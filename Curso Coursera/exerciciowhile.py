numero = int(input('Digite um número inteiro positivo: '))
while numero >=0:
    fatorial = 1
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1
    print (fatorial)
    numero = int(input('Digite um número inteiro positivo: '))

