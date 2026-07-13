# simulador de firewall
firewall = True
# loop
while firewall == True:
	ip = input("Qual é o IP? ")
	protocolo = input("Qual é o protocolo? SSH OU HTTP").upper()
	porta = int(input("Qual é o numero da porta? "))
	tamanho_do_pacote = float(input("Qual é o tamanho do pacote? MB"))
	if tamanho_do_pacote > 50.0:
		print("❌ CONEXÃO BLOQUEADA: Tamanho de pacote suspeito!")
	elif protocolo == "SSH" and porta < 1000:
		print("⚠️ ALERTA: Tentativa de acesso SSH em porta insegura!")
	else:
		print(f"✅ CONEXÃO ACEITA: Tráfego limpo para o IP {ip}..")
	continuar_firewall = input("Continuar com o firewall ligado? sim ou nao").lower()
	if continuar_firewall == "sim":
		firewall = True
	else:
		firewall = False
print("Sistemas desprotegidos. Firewall encerrado.")
