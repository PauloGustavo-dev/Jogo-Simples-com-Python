def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou=False
    acertou=False
    #looping, enquanto ele nao acerta e enquanto ele nao foi "enforcado"
    while(not enforcou and not acertou):
        chute= input("Insira uma letra: ")

        index=0
        for letra in palavra_secreta:
            if(chute.upper()==letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute,index))
            index+=1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()