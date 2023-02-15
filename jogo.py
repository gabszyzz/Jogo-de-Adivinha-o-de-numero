import random
import math

lower = int(input("Digite o limite minimo: "))
upper = int(input("Digite o limite maximo: "))

x = random.randint(lower, upper)
print("\n\tVocê só tem  ", round(math.log(upper - lower + 1, 2)), " chances de advinhar o numero inteiro!\n")

count = 0
try:
    while count < math.log(upper - lower + 1, 2):
        count += 1

        guess = int(input("Advinhe o numero: "))

        if x == guess:
            print("Parabens você acertou em ", count, " tentativas")
            break
        elif x > guess:
            print("Tente um numero maior!")
        elif x < guess:
            print("Tente um numero menor!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nO numero é %d" % x)
        print("\nMais sorte da proxima vez!")
except ValueError:
    print('Valores muito baixo! ')

