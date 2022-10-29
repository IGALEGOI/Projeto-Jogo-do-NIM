#Eric Galego Lima RA: G452DC-2

from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def computadorEscolheJogada(_numPecas, _limite):
    if _numPecas > _limite:
        pecas = _numPecas%(_limite+1)
        print("\nO computador tirou %s peça(s)" %pecas)
    else:
        pecas = _limite
        print("\nO computador tirou %s peça(s)" %pecas)
        
    return pecas
    
def usuarioEscolheJogada(_limite):
    while True:

        pecas = int(input("Quantas peças você quer tirar? "))

        if pecas > 0 and pecas <= _limite:
            break
        else:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %_limite)
            continue

    print("\nVocê tirou %s peça(s)" %pecas)
    
    return pecas

def inicio():
    print("================ SEJA BEM VINDO AO JOGO DO NIM ================")
    print("------ Vamos ver se você consegue ganhar do computador? -------\n")
    while True:
        numPecas = int(input("Quantas peças? "))
        limite = int(input("Limite de peças por jogada? "))
        if numPecas > 0 and limite > 0 and numPecas > limite:
            break
        else:
            print("\nAtenção: número e limite de peças devem ser inteiros e maiores que 0. E número de peça(s) dever ser maior que limite de peça(s)!")
            continue
    
    if numPecas%(limite+1) == 0:
        print("\nVocê começa")
        quemJoga = "usuario"
    else:
        print("\nComputador começa")
        quemJoga = "computador"
    
    while True:
        if quemJoga == "usuario":
            numPecas -= usuarioEscolheJogada(limite) 
            quemJoga = "computador"
        else:
            numPecas -= computadorEscolheJogada(numPecas,limite) 
            quemJoga = "usuario"
        
        print("Agora resta(m) %s peça(s) no tabuleiro." %numPecas)
        
        if numPecas == 0:
            if quemJoga == "usuario":
                vencedor = "computador"
                print("\nFim do jogo! O %s ganhou!" %vencedor)
                return vencedor
            else:
                vencedor = "VOCÊ"
                print("\nFim do jogo! %s ganhou!" %vencedor)
                return vencedor
        elif numPecas < limite: 
            limite = numPecas 

while True:
    clear()
    
    inicio()

    continua = input("\nDeseja continuar? Precione Enter para um novo jogo ou S para sair: ")

    if(continua == 'S' or continua == 's'):
        clear()
        break