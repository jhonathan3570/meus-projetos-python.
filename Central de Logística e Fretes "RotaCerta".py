historico_destinos = []
viagem = False 
pergunta = input("vai viajar? sim ou não").lower()
if pergunta == "sim":
    viagem = True
# loop 
while viagem == True:
    destino = input("Qual é o destino?")
    capital = input("O destino é uma capital? sim ou não")
    distancia = int(input("Qual é a distância até o destino? km"))
    gasolina = float(input("Quanto vai ser gasto com combustível nessa viagem?"))
    pedagio = input("A rota tem pedagio? sim ou não"). lower()
    if pedagio == "sim":
        pedagio = True
    else:
        pedagio = False
    historico_destinos.append(destino)
    if distancia <= 50:
        print("viagem curta")
    if distancia >= 300:
        print("viagem longa, descanso obrigatório exigido!")
    if capital == "sim":
        print("Rota obrigatória: destino a capital!")
    if gasolina <= 0:
        print("Valor invalido")
        viagem = False
    viagem2 = input("Voçê quer cadastrar outra viagem? sim ou não").lower()
    if viagem2 != "sim":
        viagem = False
print(historico_destinos)
total_viagens = len(historico_destinos)
print(f"Total de rotas processadas hoje: {total_viagens}")
