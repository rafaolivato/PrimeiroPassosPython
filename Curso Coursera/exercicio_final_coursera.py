import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\33[1;30;41m Bem-vindo ao detector automático de COH-PIAH.\33[m")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    i = 0
    f = 0
    while i < 6:
        f += abs(as_a[i] - as_b[i])
        i = i + 1
    s = f / 6

    return s


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_palavras = []
    lista_frases = []
    lista_sent = separa_sentencas(texto)
    tamanho_palavras = 0
    tamanho_sentenca = 0
    tamanho_frases = 0

    for sent in lista_sent:
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)

    for fra in lista_frases:
        novas_palavras = separa_palavras(fra)
        lista_palavras.extend(novas_palavras)

    for pal in lista_palavras:
        tamanho_palavras = tamanho_palavras + len(pal)

    wal_texto = tamanho_palavras /  len(lista_palavras)
    ttr_texto = n_palavras_diferentes(lista_palavras) /  len(lista_palavras)
    hlr_texto = n_palavras_unicas(lista_palavras) /  len(lista_palavras)

    for x in lista_sent:
        tamanho_sentenca = tamanho_sentenca + len(x)

    sal_texto = tamanho_sentenca /  len(lista_sent)
    sac_texto = len(lista_frases) / len(lista_sent)

    for y in lista_frases:
        tamanho_frases = tamanho_frases + len(y)

    pal_texto = tamanho_frases /  len(lista_frases)

    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    avalia = []

    for i in (textos):
        nova_compara = compara_assinatura(calcula_assinatura(i), ass_cp)
        avalia.append(nova_compara)

    x = min(avalia)

    i = 0
    while i <= len(avalia) - 1:
        if avalia[i] == x:
            y = i + 1
            i = len(avalia)
        else:
            i = i + 1

    return y


x = le_assinatura()
y = le_textos()
z = avalia_textos(y, x)

print("\33[2;30;40m O Autor do texto", z, "Está infectado com COH-PIAH")
