def validar_amostra(id_amostra):
    # Retorna True se for diferente de 0, False se for igual a 0
    return id_amostra != 0
def avaliar_estabilidade(temperatura, ph):
    if temperatura <= 5 and ph <=8:
        return "amostra estavel"
    elif temperatura <= 15 and ph <= 14:
        return "ALERTA: Anomalia de pH"
    elif temperatura >= 24 and ph >= 20:
        return "CRÍTICO: Risco de Morte Celular"
amostras = []        
pergunta = input("quer auditar amostras?").lower()
resposta = (pergunta == "sim")
while resposta == True:
    id_amostra = int(input("id da amostra"))
    if validar_amostra(id_amostra) == True:
        nome = input("nome da amostra")
        temperatura = float(input("Temperatura da amostra"))
        ph_nivel =float(input("nível de ph"))
        seguranca = input("amostra representa perigo biologico? sim ou não").lower()
        seguranca_resposta = (seguranca == "sim")
        avaliacao = avaliar_estabilidade(temperatura, ph_nivel)
        ficha = {
            "nome": nome,
            "id": id_amostra,
            "temperatura": temperatura,
            "ph": ph_nivel,
            "segurança": seguranca_resposta,
            "avaliação": avaliacao,
        }
        amostras.append(ficha)
        pergunta = input("Continuar auditando amostras? sim ou não").lower()
        if pergunta != "sim":
            resposta = False
print("inspeção da amostra")
print(amostras)
