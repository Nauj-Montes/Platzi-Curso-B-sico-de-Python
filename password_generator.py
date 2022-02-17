import random
import string


def random_password():
    ALL_CHARACTERS = string.ascii_lowercase + string.digits + \
        string.punctuation + string.ascii_uppercase
    password = ""

    for i in range(16):
        password += random.choice(ALL_CHARACTERS)

    return password


def main():
    suggested_password = random_password()
    print("\nMay I suggest, using this extremely secure password? : " +
          suggested_password + " 🍷🧐\n")


if __name__ == "__main__":
    main()
