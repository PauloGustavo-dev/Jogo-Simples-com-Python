import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("----------------------------")
        forca.jogar()
    elif(jogo == 2):
        print("----------------------------")
        adivinhacao.jogar()
    else:
        print("Opção Invalida")

if(__name__ == "__main__"):
    escolhe_jogo()
