def main():
    user_max_number = max_number_generator()
    print(prime_number_generator(user_max_number))
def max_number_generator():
    return int(input('Up to what number do you want to generate?: '))
def prime_number_generator(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, limit + 1, i):
                primes[multiple] = False
    return [i for i, is_p in enumerate(primes) if is_p]
if __name__ == "__main__":
    main()