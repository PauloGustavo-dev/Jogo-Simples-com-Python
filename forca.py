import random

def jogar():
    
    mensagem_de_abertura()

    palavra_secreta=carrega_palavra_secreta()

    #lista de caracteres que serão substituidos conforme o usuario acerta 
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou=False
    acertou=False
    erros=0

    #looping, jogo roda enquanto ele nao acerta e enquanto ele nao foi "enforcado"
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
        print("Voce perdeu, a palavra era",palavra_secreta)

def mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras=[]

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero= random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

if(__name__ == "__main__"):
    jogar()