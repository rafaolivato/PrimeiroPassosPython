decrescente = True
anterior = int(input("digite o primeiro número da sequencia  ",  ))
valor = 1
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo da sequência  " ,  )) 
    if valor >= anterior:
        decrescente = False
    anterior = valor
if decrescente == True:
    print(" A sequência está em ordem decrescente")
else:
    print(" A sequência não está em ordem decrescente :-(")
    