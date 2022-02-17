def palindromo(palabra):
    if palabra.lower().replace(" ", "") == palabra.lower().replace(" ", "")[::-1]:
        return "Es palíndromo ✔"
    else:
        return "No es palíndromo ❌"


def main():
    print(palindromo(input("Escribe un palabra: ")))


if __name__ == "__main__":
    main()
