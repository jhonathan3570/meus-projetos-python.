# 1. Nome da lista padronizado com 'b' minúsculo
banco_de_alvos = []

perfis = int(input("Quantos perfis vão ser cadastrados? "))

for perfil in range(perfis):
    print(f"\n--- Cadastrando Perfil {perfil + 1} de {perfis} ---")
    nome = input("Qual é o nome? ")
    codinome = input("Qual o codinome? ")
    codigo = int(input("Qual é o ID? "))
    postagens_suspeitas = int(input("Quantidade de postagens suspeitas analisadas: "))
    automacao = float(input("Índice de automação: "))
    alvo_input = input("O alvo é considerado de alta prioridade? (sim ou não): ").lower()
    
    # Converte a resposta em booleano (True/False)
    alvo_prioridade = (alvo_input == "sim")

    # 2. Validação do ID feita ANTES de criar o dicionário
    if codigo == 0:
        print("🚨 ID inválido detectado!")
        id_final = "inválido"
    else:
        id_final = codigo

    # Dicionário com chaves limpas (sem espaços ou dois pontos)
    ficha = {
        "nome": nome,
        "codinome": codinome,
        "id": id_final,
        "postagens_suspeitas": postagens_suspeitas,
        "automacao": automacao,
        "alta_prioridade": alvo_prioridade,
    }

    # Adiciona a ficha na lista a cada volta do loop
    banco_de_alvos.append(ficha)

    # Regras de alerta
    if automacao <= 20.0:
        print("🟢 Baixo nível de automação!")
    elif automacao >= 80.0:
        print("🔴 Alerta! Alto índice de automação.")

    if alvo_prioridade == True:
        print("⚠️ Alvo de alta periculosidade e prioridade!")

# Relatório final impresso fora do loop
print("\n==========================================")
print("📊 BANCO DE ALVOS REGISTRADO:")
print(banco_de_alvos)
