def outputJsonFeedbackConsultants(dados):
    saida =[]
    for dado in dados:
        saida.append({"id":dado.id, "projectLaw":dado.projectLaw, "amendment":dado.amendment,"topic":dado.topic,
                      "matConsultant":dado.matConsultant,"dataAlteracao":str(dado.dataAlteracao)})
    return saida

def outputJsonFeedbackConsultant(dado):
    return {"id":dado.id, "projectLaw":dado.projectLaw, "amendment":dado.amendment,
            "topic":dado.topic,
            "matConsultant":dado.matConsultant,
            "dataAlteracao":str(dado.dataAlteracao)}