def is_prime(number):
    condition = 0
    for i in range(1, number + 1):
        if number % i == 0:
            condition += 1

    if condition > 2:
        return False
    else:
        return True


def run():
    prime_numbers = []
    for x in range(2, 101):
        if is_prime(x):
            prime_numbers.append(x)
    print(prime_numbers)


if __name__ == "__main__":
    run()
