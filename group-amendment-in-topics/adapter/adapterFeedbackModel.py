
def outputJsonFeedbackModels(dados):
    saida =[]
    for dado in dados:
        saida.append({"id":dado.id, "projectLaw":dado.projectLaw, "amendment":dado.amendment,"topic":dado.topic,"score_standardized":dado.score_standardized})
    return saida

def outputJsonFeedbackModel(dado):
    return {"id":dado.id, "projectLaw":dado.projectLaw, "amendment":dado.amendment,"topic":dado.topic,"score_standardized":dado.score_standardized}