# n: número de peças iniciais
# m: número máximo de peças que podem ser retiradas
#n >= m
def computador_escolhe_jogada(n,m):
    i = m
    while (n-i)%(m+1)!= 0:
        i = i - 1
    return i    

def usuario_escolhe_jogada(n,m):
    u = n + 1
    indicador = False
    while not indicador:
        u = int(input("Quantas peças você vai tirar? \n" ))
        if (u > m) or (u <= 0) or (type(u) == str):
            print("Oops! Jogada inválida! Tente de novo \n")
        else:
            indicador = True
    return u

def partida():
    indicador = True
    c=0
    u=0
    usComeca = False
    n=m=0
    n = int(input("Quantas peças? \n"))
    m = int(input("Limite de peças por jogada? \n"))

    if n % (m+1) == 0:
        print("Você começa! \n")
        usComeca = True
    else:
        print("Computador começa! \n") ##Pensar num jeito de determinar essa  
                                    # ordem de maneira eficiente
    while indicador:
        if usComeca:
            u = usuario_escolhe_jogada(n,m)
            n = n - u 
            print("Você tirou", u ,"peça(s) \n")  
            if n == 0:
                print("Você ganhou! \n")
                indicador = False
                return 0             #Se o jogador ganha a função retorna 0
            else:
                print("Agora restam", n ,"peça(s) \n")

        usComeca = True
        c = computador_escolhe_jogada(n,m)
        n = n - c
        print("O computador tirou", c ,"peça(s) \n")
        if n == 0:
            print("O computador ganhou! \n")
            return 1            #Se o computador ganha a função retorna 1
            indicador = False
        else:
            print("Agora restam", n ,"peça(s) \n")

def campeonato():
    i = 1
    us = 0 
    pc = 0
    while i <= 3:
        print("***Rodada", i,"*** \n")        
        if partida() == 1:
            pc = pc + 1
        else:
            us = us + 1
        i = i + 1
    print("***Fim de Campeonato!*** \n")
    print("Placar: Você", us ,"X", pc ,"Computador")

print("Bem-vindo ao jogo do NIM! Escolha: \n")
a = int(input("1 - para jogar partida isolada \n2 - para jogar um campeonato \n"))
if a == 1:
    print("Você escolheu uma partida isolada! \n")
    partida()
else:
    print("Você escolheu um campeonato! \n")
    campeonato()
