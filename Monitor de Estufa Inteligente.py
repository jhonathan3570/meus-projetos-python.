monitoramento = False

# Pergunta inicial
pergunta_monitoramento = input("Voce quer abrir o monitoramento? (sim/nao): ").lower()
if pergunta_monitoramento == "sim":
    monitoramento = True

# Loop de monitoramento
while monitoramento == True:
    setor_ou_pranta = input("Qual é o nome da planta ou setor? ")
    temperatura_atual = float(input("Qual é a temperatura atual? "))
    irrigacao = int(input("Quantas vezes o solo já foi irrigado hoje? "))
    
    # Decisão 1: Verificação de Temperatura
    if temperatura_atual <= 15.0:
        print("🔥 Aquecimento ligado!")
    if temperatura_atual >= 35.0:
        print("⚠️ ALERTA: Superaquecimento!!!") 
    
    # Decisão 2: Verificação de Irrigação usando um Booleano de verdade
    # Isso transforma a resposta em True (se for sim) ou False (se for nao)
    precisa_irrigar = input("O solo está seco e precisa de água? (sim/nao): ").lower() == "sim"
    
    if precisa_irrigar == True:
        irrigacao += 1
        print(f"💧 Irrigação ativada! Novo total de regas hoje: {irrigacao}")
    else:
        print(f"✅ Solo em condições ideais. Total de regas: {irrigacao}")
        
    # Controle de saída do loop
    pergunta = input("Você quer continuar com o monitoramento? (sim/nao): ").lower() 
    if pergunta != "sim":
        monitoramento = False

print("O monitoramento está fechado.")
