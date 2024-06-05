import random

numero_aleatorio = random.randint(1, 10)
chute_usuario = input("Digite um numero de 0 a 10: ")


chute_numero_int = int(chute_usuario)
    
if chute_numero_int == numero_aleatorio:
        print ('Você acertou, parabéns!')
    
while chute_numero_int !=  numero_aleatorio :
    print('Tente novamente, voce errou!')
    chute_usuario = int(input("Digite um numero de 0 a 10: "))

    
    if chute_usuario == numero_aleatorio:
        print(f'Parabens voce acertou, o numero al2atório é {numero_aleatorio}!!')
        break

    