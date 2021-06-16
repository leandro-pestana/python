print("Jogo do Adivinha")

numero_secreto = 42
numero_de_tentativa = 3
rodada = 1

while(rodada <= numero_de_tentativa):
    print("Tentativa", rodada, "de", numero_de_tentativa)
    chute_str = input("Digite um número")
    print("Você Digitou", chute_str)

    chute = int(chute_str)
    acertou = (numero_secreto == chute)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if(acertou):
        print("Você acertou, parabens!")
    else:
        if(maior):
            print("Você errou, seu chute foi alto")
        elif(menor):
            print("Você errou, seu chute foi baixo")

    rodada = rodada + 1
