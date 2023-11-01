from model.bm25 import *
import numpy as np
import math
from util.util import QUANT_TOPIC,K1,B,EPSILON

class BM25L(BM25):
    def __init__(self, corpus, tokenizer=None, k1=K1, b=B, epsilon=EPSILON):
        self.k1 = k1
        self.b = b
        self.epsilon = epsilon
        super().__init__(corpus, tokenizer)

    # Calculo do IDF (Inverse Document Frequency)
    def _calc_idf(self, nd):
        # collect idf sum to calculate an average idf for epsilon value
        idf_sum = 0
        # collect words with negative idf to set them a special epsilon value.
        # idf can be negative if word is contained in more than half of documents
        negative_idfs = []
        for word, freq in nd.items():
            idf = math.log(self.corpus_size + 1) - math.log(freq + 0.5)
            self.idf[sys.intern(word)] = idf
            idf_sum += idf
            if idf < 0:
                negative_idfs.append(word)
        self.average_idf = idf_sum / len(self.idf)

        eps = self.epsilon * self.average_idf
        for word in negative_idfs:
            self.idf[sys.intern(word)] = eps

    # Calculo do ctd
    def get_ctd(self, q_freq, b, doc_len, avg_len):
        ctd = q_freq/(1 - b + b*(doc_len)/(avg_len))
        return ctd

    # Avaliar a pontuacao de todos os documentos na base
    def get_scores(self, query):
        score = np.zeros(self.corpus_size)
        doc_len = np.array(self.doc_len)

        # Funcionamento de term_freqs e term_docs
        # Ex: term_freqs['termo'] = [10, 5, 4, 15] => frequências do termo (TF > 0)
        #     term_docs['termo'] = [5, 20, 40, 55] => termo ocorre nos docs 5, 20, 40, 55
        for q in query:
            if q not in self.term_freqs:
                continue
            q_tf = [0]*self.corpus_size
            for docn, tf in zip(self.term_docs[q], self.term_freqs[q]):
                q_tf[docn] = tf
            ctd = q_tf / (1 - self.b + self.b * (doc_len) / (self.avgdl))
            score += (self.idf.get(q, 0)) * ((ctd + 0.5) * (self.k1 + 1) / ((ctd + 0.5) + self.k1))

        return score

    def get_top_n(self, query, documents, n=QUANT_TOPIC):

        assert self.corpus_size == len(documents), "The documents given don't match the index corpus"

        scores = self.get_scores(query)

        if np.isclose(np.max(scores), np.min(scores), atol=1e-5):
            score_ref = 1.0 if np.max(scores) > 1e-6 else 0.0
            scores_normalized = np.array([score_ref for i in range(len(scores))])
        else:
            scores_normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

        scores_final = np.copy(scores_normalized)

        top_n = np.argpartition(scores_final, -n)[::-1][:n]
        top_n = top_n[np.argsort(scores_final[top_n])[::-1]]

        return [documents[i].tolist()[0] for i in top_n]