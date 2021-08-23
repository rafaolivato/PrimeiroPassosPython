largura = int(input("Digite a largura: "))

altura = int(input("Digite a altura: "))

caractere = "#"

def retângulo(largura, altura, caractere):
    linha_cheia = caractere * largura

    if largura > 2:

        linha_vazia = caractere + (" " * (largura - 2)) + caractere

    else:

        linha_vazia = linha_cheia

    if altura >= 1:
        print(linha_cheia)

    for i in range(altura - 2):
        print(linha_vazia)

    if altura >= 2:
        print(linha_cheia)


retângulo(largura, altura, caractere)

