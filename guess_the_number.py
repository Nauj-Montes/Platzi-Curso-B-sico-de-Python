import random


def guess_number():
    to_guess = random.randint(1, 100)
    guess = 0

    while guess != to_guess:
        guess = int(input("\nPor favor, ingrese un numero: "))

        if guess > to_guess:
            print("Prueba con un número más pequeño\n")
        elif guess < to_guess:
            print("Prueba con un número más grande\n")
        else:
            print("¡Acertaste!🤑👌")


def run():
    guess_number()


if __name__ == "__main__":
    run()
