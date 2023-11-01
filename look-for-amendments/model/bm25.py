import numpy as np
import sys
from multiprocessing import Pool, cpu_count


DEFAULT_CUT = 0.4
DEFAULT_DELTA = 0.1

class BM25:
    def __init__(self, corpus, tokenizer=None):
        self.corpus_size = len(corpus)
        self.avgdl = 0
        self.idf = {}
        self.doc_len = []
        self.tokenizer = tokenizer
        self.term_freqs = {} # dicionário para guardar os "term frequencies" (TF), da forma {'termo': [lista de frequências onde freq > 0], ...}
        self.term_docs = {} # dicionário para guardar os documentos onde ocorre cada termo {'termo': [lista de docs onde ocorre 'termo'], ...}

        if tokenizer:
            corpus = self._tokenize_corpus(corpus)

        nd = self._initialize(corpus)
        self._calc_idf(nd)

    def _initialize(self, corpus):
        num_doc = 0
        doc_n = 0  # nº do documento
        for document in corpus:
            self.doc_len.append(len(document))
            num_doc += len(document)

            # dicionário para controlar quebra de documento para cada n-grama
            doc_changed = {}
            for word in document:
                doc_changed[sys.intern(word)] = True # significa que mudou o documento; indica para todas as palavras do documento

            for word in document:
                # Incrementa o dicionário de TF
                if word not in self.term_freqs:
                    self.term_freqs[sys.intern(word)] = [1]
                    self.term_docs[sys.intern(word)] = [doc_n]
                    doc_changed[sys.intern(word)] = False
                else:
                    if not doc_changed[sys.intern(word)]:
                        self.term_freqs[sys.intern(word)][-1] += 1  # incrementa frequência do termo no documento = TF(t, d)
                    else:
                        self.term_freqs[sys.intern(word)].append(1)
                        self.term_docs[sys.intern(word)].append(doc_n)
                        doc_changed[sys.intern(word)] = False
            doc_n += 1

        # monta o dicionário DF (Document Frequency)
        df = {}
        for term_freq, lst_freqs in zip(self.term_freqs.keys(), self.term_freqs.values()):
            df[sys.intern(term_freq)] = len(lst_freqs)

        self.avgdl = num_doc / self.corpus_size
        return df

    def _tokenize_corpus(self, corpus):
        pool = Pool(cpu_count())
        tokenized_corpus = pool.map(self.tokenizer, corpus)
        return tokenized_corpus

    def _calc_idf(self, nd):
        raise NotImplementedError()

    def get_scores(self, query):
        raise NotImplementedError()

    def get_batch_scores(self, query, doc_ids):
        raise NotImplementedError()

    def get_top_n(self, query, documents, n=5):

        assert self.corpus_size == len(documents), "The documents given don't match the index corpus"

        scores = self.get_scores(query)
        try:
            scores_normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))
        except:
            scores_normalized = [0 for i in range(scores)]

        top_n = np.argsort(scores)[::-1][:n]
        return [documents[i] for i in top_n], np.sort(scores)[::-1][:n], np.sort(scores_normalized)[::-1][:n], np.sort(
            scores)[::-1][:n]

