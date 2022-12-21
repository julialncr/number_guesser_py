import random

print("Bem-vindo ao programa de adivinhar um número de 0 a 10!")

random_number = random.randint(0,10)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Tente adivinhar: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Por favor, digite um número")
        continue

    if user_guess == random_number:
        print("Você acertou!")
        break
    elif user_guess > random_number:
        print("É um número menor...")
    else:
        print("É um número maior...")

print("Você acertou em", guesses, "tentativa(s)!")