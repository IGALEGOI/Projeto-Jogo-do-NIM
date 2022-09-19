from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

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

        r = int(input("Quantas peças você quer tirar? "))

        if r > 0 and r <= m:
            break
        else:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %m)
            continue
    print("\nVocê tirou %s peça(s)" %r)
    
    return r

def inicio():
    print("====="," BEM VINDO AO JOGO DO NIM ","=====")
    print("---"," Tente ganhar do computador ","---")
    while True:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n > 0 and m > 0 and n > m:
            break
        else:
            print("\nAtenção: número e limite de peças devem ser inteiros maiores que 0. E número dever ser maior que limite de peça(s)")
            continue
    
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

while True:
    clear()
    
    inicio()

    continua = input("\nDeseja continuar? Precione Enter para um novo jogo ou S para sair: ")

    if(continua == 'S' or continua == 's'):
        clear()
        break