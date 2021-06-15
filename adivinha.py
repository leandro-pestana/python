print("Jogo do Adivinha")

numero_secreto = 42


chute_str = input("Digite um número")
print("Você Digitou", chute_str)

chute = int(chute_str)
if(numero_secreto == chute):
    print("Você acertou, parabens!")
else:
    print("Você errou, tente novamente")
