
 
def main():
 
    print("\nBem-Vindo ao jogo do NIM! Escolha:\n")
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    print()
     
    if escolha == 1:
        partida()
 
    else:
        campeonato()
 
 
def usuario_escolhe_jogada(n, m):
 
    escolheu = False
    peças_usuario = 0
    
    while not escolheu:
        peças_usuario = int(input("Quantas peças você vai tirar? "))
 
        if peças_usuario > m or peças_usuario <= 0 or peças_usuario > n:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            escolheu = True
 
    return peças_usuario        
 
    
def computador_escolhe_jogada(n, m):
 
    peças_cpu = 0
 
    if n % (m+1) != 0:
        while n % (m+1) != 0:
            n -= 1
            peças_cpu += 1
 
    else:
        n = n - m
        peças_cpu = m
 
    return peças_cpu        
 
 
def campeonato():
 
    rodada = 1
    placar_cpu = 0
    placar_usuario = 0
    print("Voce escolheu um campeonato!")
 
    while rodada <= 3:
 
        print()
        print("**** Rodada", rodada," ****\n")
        cpu_ganha = partida()
 
        if cpu_ganha:
 
            placar_cpu += 1
 
        else:
 
            placar_usuario += 1
 
        rodada += 1    
 
    print()
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario,"X",placar_cpu,"Computador")
 
 
def partida():
 
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    cpu_ganha = False
    n_dif_zero = True
       
    
    if n % (m + 1) != 0:
        print("Computador começa!\n")
 
        while n > 0:
 
            n_cpu = computador_escolhe_jogada(n,m)
            n = n - n_cpu
 
            if n == 0:
                n_dif_zero = not n_dif_zero
                cpu_ganha = True
 
            if n_cpu == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", n_cpu,"peças.")
 
            if n_dif_zero:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro\n")
                else:
                    print("Agora restam", n,"peças no tabuleiro.\n")
                     
            #jogada do usuário
                     
            if n > 0:
 
                n_usuario = usuario_escolhe_jogada(n, m)
                n = n - n_usuario
 
                if n == 0:
                     n_dif_zero = not n_dif_zero
                
                if n_usuario == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou", n_usuario,"peças.")    
 
                if n_dif_zero:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro\n")
                    else:
                        print("Agora restam", n,"peças no tabuleiro.\n")    
        
        if cpu_ganha:
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Você ganhou!")
            
    #***USUÁRIO COMEÇA*******
            
    else:
        print("Você começa!\n")
 
        while n > 0:
 
            n_usuario = usuario_escolhe_jogada(n, m)
            n = n - n_usuario
 
            if n == 0:
                n_dif_zero = not n_dif_zero
                
            if n_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", n_usuario,"peças.")    
 
            if n_dif_zero:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro\n")
                    else:
                        print("Agora restam", n,"peças no tabuleiro.\n") 
            
            #jogada do computador
                    
            if n > 0:
 
                n_cpu = computador_escolhe_jogada(n,m)
                n = n - n_cpu
 
                if n == 0:
                     n_dif_zero = not n_dif_zero
                     cpu_ganha = True      
 
                if n_cpu == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou", n_cpu,"peças.")
            
                if n_dif_zero:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro\n")
                    else:
                        print("Agora restam", n,"peças no tabuleiro.\n")
 
        if cpu_ganha:
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Você ganhou!")
 
    return cpu_ganha
	
main()