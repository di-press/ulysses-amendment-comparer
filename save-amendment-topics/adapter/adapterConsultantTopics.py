def outputJsonAllConsultantTopics(dados):
    saida =[]
    for dado in dados:
        saida.append({"id":dado.id, "projectLaw":dado.projectLaw, 
                        "topic_id":dado.topic_id,"topic":dado.topic,
                        "topic_description":dado.topic_description,
                        "matConsultant":dado.matConsultant,
                        "dataAlteracao": str(dado.dataAlteracao)})
    return saida

def outputJsonConsultantTopics(dado):
    return {"id":dado.id, "projectLaw":dado.projectLaw, 
            "topic_id":dado.topic_id,
            "topic":dado.topic,
            "topic_description":dado.topic_description,
            "matConsultant":dado.matConsultant,
            "dataAlteracao": str(dado.dataAlteracao)}
