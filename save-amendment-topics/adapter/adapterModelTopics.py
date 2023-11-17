
def outputJsonAllModelTopics(dados):
    saida =[]
    for dado in dados:
        saida.append({"id":dado.id, "projectLaw":dado.projectLaw, 
        "topic_id":dado.topic_id, "terms":dado.terms,
        "configuration":dado.configuration})
    return saida

def outputJsonModelTopics(dado):
    return {"id":dado.id, "projectLaw":dado.projectLaw, 
        "topic_id":dado.topic_id, "terms":dado.terms,
        "configuration":dado.configuration}