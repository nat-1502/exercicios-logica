numero = int(input('Digite um numero para saber o fatorial dele '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero +1):
        fatorial = fatorial * item
        
    print(fatorial)