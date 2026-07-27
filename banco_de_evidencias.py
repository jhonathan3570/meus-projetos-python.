banco_de_evidencias = []
sistema = input("Quer adicionar informações? sim ou não"). lower()
if sistema == "sim":
    sistema = True
else:
    sistema = False

while sistema == True:
    # inputs de entrada
    evidencia = input("evidência: ")
    numero_da_amostra = int(input("Numero de identificação: "))
    pureza = float(input("Nivel de pureza: "))
    custodia_input = input("A custódia está intacta? violada ou lacradra").lower()
    custodia = (custodia_input == "lacrada")
    massa = float(input("Massa: "))    
    # dicionário 
    ficha = {
        "evidência": evidencia,
        "numero de identificação": numero_da_amostra,
        "pureza da amostra": pureza,
        "custódia": custodia,
        "massa": massa,
    }    
    # colocando o dicionário na lista
    banco_de_evidencias.append(ficha)
    # chegarem das regras
    if massa <= 5.0:
        print("massa abaixo dos requisitos")
        sistema = False
    if pureza >= 95.0:
        print("evidência identificada com grande relevância!")
    if numero_da_amostra == 0:
        print("ID nao valido detectado!")
        sistema = False
    pergunta = input("Quer adicionar mais informações? sim ou não"). lower()
    if pergunta != "sim":
        print("sistema fechado")
        sistema = False
print(banco_de_evidencias)   
