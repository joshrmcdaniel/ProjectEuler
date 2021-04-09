import sys

def main(num):
    primes = [i for i in range(2, int(num ** .5) + 1) if num % i == 0 and prime(i)]
    print(primes)


def prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** .5) + 1):
        if num % i == 0:
            return False

    return True

if __name__ == '__main__':
    main(int(sys.argv[1]))
