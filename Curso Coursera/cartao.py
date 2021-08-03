meucartao = int(input("Digite o número do seu cartão de crédito"))
cartaolido = 1
encontreimeucartaonalista = False
while cartaolido!= 0 and not encontreimeucartaonalista:
    cartaolido = int(input("Digite o número do próximo cartão de crédito  "))
    cartaodecredito: " "
    if cartaolido == meucartao:
     encontreimeucartaonalista= True
if encontreimeucartaonalista:
    print("Eba, !!! Meu cartão está lá!!!")
else:
    print("Xi, meu cartão não está lá")
