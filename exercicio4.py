


velocida_usuario = int(input('Digite a velocidade que você passou na via '))

vel_max = 80


if velocida_usuario <= vel_max:
    print ("Você está abaixo da velocidade, não se preocupe!")
elif velocida_usuario >= 81 and velocida_usuario <= 90 :
    print ("Você levou multa leve!")
elif velocida_usuario >= 91 and velocida_usuario <= 100:
    print ("Você levou multa grave!")
elif velocida_usuario >= 101:
    print ("Você levou multa gravissíma!")

