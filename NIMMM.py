def usuario_escolhe_jogada(n, m):
    a = True
    while a == True:
        b = True
        retira = int(input("Quantas peça(s) você vai tirar? "))
        print()
        if retira > int(m) or retira < 0 or retira > int(n):
                       print("Oops! Jogada inválida! Tente de novo")
                       print()
                       b = False

        if retira <= int(m) and retira > 0 and b == True:
                       a = False
                       n = int(n) - retira
                       return retira
                       print()
                       



def computador_escolhe_jogada(n, m):
    a = True
    if int(n) >= int(m) and n != 0:
        b = int(m) + 1
        c = m
        while a == True:
            sobra = int(n) - int(c)
            verif = int(sobra) % int(b)

            if int(verif) == 0 and c > 0:
                return c

            if int(c) > 0:
                c = int(c) - 1

            if int(c) <= 0:
                return m 


    if int(m) > int(n) and n!= 0:
        return n 




def partida():
    n = int(input("Quantas peças terá no jogo? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    resultado = n % (m + 1)
    if resultado == 0:
        print("Você começa!")
        print()
        while n > 0:
            u = usuario_escolhe_jogada(n, m)
            print("Você retirou",u,"peça(s).")
            n = n - int(u)
            print("Agora restam",n,"peças no tabuleiro.")
            print()
            if n == 0:
                print("Fim de jogo! Você Ganhou!")
                print()
                break

            c = computador_escolhe_jogada(n, m)
            print("O Computador retirou",c,"peça(s).")
            n = n - int(c)
            print("Agora restam",n,"peça(s) no tabuleiro.")
            print()
            if n == 0:
                print("Fim de Jogo! O Computador ganhou!")
                print()
                return 1

    if resultado != 0:
        print("O Computador começa!")
        print()
        while n > 0:
            c = computador_escolhe_jogada(n, m)
            print("O Computador retirou",c,"peça(s).")
            n = n - int(c)
            print("Agora restam",n,"peça(s) no tabuleiro.")
            print()
            if n == 0:
                print("Fim de Jogo! O Computador ganhou!")
                print()
                return 1

            u = usuario_escolhe_jogada(n, m)
            print("Você retirou",u,"peça(s).")
            n = n - int(u)
            print("Agora restam",n,"peças no tabuleiro.")
            print()
            if n == 0:
                print("Fim de jogo! Você Ganhou!")
                print()
                break


def campeonato():
    i = 1
    while i <= 3:
        print("***** Rodada",i,"*****")
        print()
        a = partida()
        i += 1
        s = a + 1
        s += 1

    print("***** Final do Campeonato! *****")
    print("Placar: Você 0","x",s,"Computador")



def main():
    print("Bem-vindx ao NIM!")
    print()
    print("Escolha qual modo você quer jogar...")
    j = int(input("1 - Partida Única ou 2 - Campeonato: "))
    print()
    if j == 1:
        print("Você escolheu Partida Única!")
        print()
        print("Começou!")
        print()
        partida()

    if j == 2:
        print("Você escolheu Campeonato!")
        print()
        campeonato()


main()




    
            
    
    
    






















