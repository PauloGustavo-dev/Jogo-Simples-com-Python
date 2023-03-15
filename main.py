import random
print("Jogo: Adivinhação!")

numero_secreto= random.randrange(1,101)
tentativas= int(input("Quantas tentativas voce deseja para o jogo? "))

for rodada in range(1,tentativas + 1):
    print("------------------------------------------")
    print("Tentativa {} de {}".format(rodada,tentativas))
    try:
        chute = input("digite um numero entre 1 e 100: ")
        chute= int(chute)
    except:
        print("digite apenas numeros")
        chute = input("digite um numero entre 1 e 100: ")
        chute= int(chute) 

    while (chute < 1 or chute > 100):
        print("------------------------------------------")
        print("Voce deve digitar um, numero entre 1 e 100")
        chute = input("digite um numero entre 1 e 100: ")
        chute= int(chute)
    
    if chute==numero_secreto:
        print("Ganhou o jogo")
        break
    elif(chute>numero_secreto):
        print("O seu numero foi maior que o numero secreto")
    else:
        print("O seu numero foi menor que o numero secreto")
    if rodada == tentativas:
        print("O numero secreto era ",numero_secreto)
print("Fim do jogo")
