# quebrar o problema em problemas menores

def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', mínima(temperaturas),'C.')
    print(' A maior temperatura o mês foi: ', máxima(temperaturas), 'C.')

    def mínima(temps):
        min = temps[0]
        i = 0
        while i < len(temps):
            if temps[i] < min:
                min = temps [i]
            i = i + 1
        return min

    #teste automatizado

    def testa_minima():
        print('Iniciando os testes')
        teste_pontual([0], 0)
        teste_pontual([0,0,0,0,0,0,0], 0)
        teste_pontual([0,1,2,3,4,5,6,7,8,9,10], 0)
        teste_pontual([30,27,25,26,29], 0)
        teste_pontual([-15, -12,0,20,30], 0)
        print('Finalizando o teste')

        def teste_pontual(temp, valor_esperado):
            valor_calculado = mínima(temp)
            if valor_calculado != valor_esperado:
                print('Valor errado para array ', temp)
                print('O valor esperado: ', valor_esperado, 'valor calculado: ')

        #refatoração - melhora o código( aqui tem muitos códigos duplicados)

testa_minima()

MinMax()
