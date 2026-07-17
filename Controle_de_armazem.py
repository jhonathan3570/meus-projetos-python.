armazen_aberto = False
pergunta = input("Você quer entrar no gerenciamento de produtos ao armazém? sim ou não"). lower()
if pergunta == "sim":
    armazen_aberto = True
while armazen_aberto == True:
   nome_do_produto = input("Qual é o nome do produto?")
   unidades = int(input("Ha quantas unidades?"))
   preco_do_produto = float(input("Qual é o preço?"))
   item_perecivel = input("item é perecível? sim ou não").lower()
   if preco_do_produto <= 0:
       print("Valor invalido, insira outro valor")
   if unidades <= 5:
      print("Reposição Urgente")
   if preco_do_produto >= 100.00:
      print("Produto Premium")
   if item_perecivel != "sim":
      print("o item não é perecível")
   pergunta_final = input("Voçê quer continuar").lower()
   if pergunta_final != "sim":
      armazen_aberto = False
print("o controle do armazem esta fechado!")             
