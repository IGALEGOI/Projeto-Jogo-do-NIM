from xml.dom.expatbuilder import parseString

def computadorEscolheJogada(n,m):
    if n > m:
        r = n%(m+1)
        print("\nO computador tirou %s peça(s)" %r)
    else:
        r = m
        print("\nO computador tirou %s peça(s)" %r)
        
    return r
    
def usuarioEscolheJogada(m):
    while True:
        try:
            r = int(input("Quantas peças você vai tirar? "))
        except:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %m)
            continue
        if r > 0 and r <= m:
            break
        else:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %m)
            continue
    print("\nVocê tirou %s peça(s)" %r)
    
    return r

def partida():
    """n, number of pieces on table; m, maximum number of pieces to be removed;"""
    enterMsg1 = "Quantas peças? "
    enterMsg2 = "Limite de peças por jogada? "
    while True:
         try:
            n = int(input(enterMsg1))
            m = int(input(enterMsg2))
            if n > 0 and m > 0 and n > m:
                break
            else:
                print("\nAtenção: 'n' e 'm' devem ser inteiros maiores que 0 e 'n' dever ser maior que 'm'")
                continue
         except:
            print("\nPor favor insira somente números inteiros maiores que 0!\nAtenção: 'n' dever ser maior que 'm'")
    
    if n%(m+1) == 0:
        print("\nVocê começa")
        quemJoga = "usuario"
    else:
        print("\nComputador começa")
        quemJoga = "computador"
    
    while True:
        if quemJoga == "usuario":
            n -= usuarioEscolheJogada(m) 
            quemJoga = "computador"
        else:
            n -= computadorEscolheJogada(n,m) 
            quemJoga = "usuario"
        
        print("Agora resta(m) %s peça(s) no tabuleiro." %n)
        
        if n == 0:
            if quemJoga == "usuario":
                vencedor = "computador"
                print("\nFim do jogo! O %s ganhou!" %vencedor)
                return vencedor
            else:
                vencedor = "VOCÊ"
                print("\nFim do jogo! %s ganhou!" %vencedor)
                return vencedor
        elif n < m: 
            m = n 

print(5*"="," BEM VINDO AO JOGO DO NIM ",5*"=")
print(3*"-"," Tente ganhar do computador ",3*"-")
partida()