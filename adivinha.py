import random

print("Jogo do Adivinha")

numero_secreto = random.randrange(1, 101)
numero_de_tentativa = 3
print(numero_secreto)

for rodada in range(1, numero_de_tentativa + 1):
    print("Tentativa {} de {}" .format(rodada, numero_de_tentativa))
    chute_str = input("Digite um número entre 1 e 100!")
    print("Você Digitou", chute_str)

    chute = int(chute_str)
    acertou = (numero_secreto == chute)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if(chute < 1 or chute > 100):
        print("Digite um número entre 1 e 100!")
        continue

    if(acertou):
        print("Você acertou, parabens!")
        break
    else:
        if(maior):
            print("Você errou, seu chute foi alto")
        elif(menor):
            print("Você errou, seu chute foi baixo")

    rodada = rodada + 1

print("Fim do Jogo")
