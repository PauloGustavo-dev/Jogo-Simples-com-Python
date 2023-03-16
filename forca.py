def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou=False
    acertou=False
    erros=0

    #looping, enquanto ele nao acerta e enquanto ele nao foi "enforcado"
    while(not enforcou and not acertou):
        chute= input("Insira uma letra: ")
        chute= chute.strip().upper()
        
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute==letra):
                    letras_acertadas[index]=letra
                index+=1
        else:
            erros+=1

        enforcou = erros==6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabens, voce ganhou")
    else:
        print("Voce perdeu")
         
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()