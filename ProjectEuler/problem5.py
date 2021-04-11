def main():
    sum = 2520
    while any(sum % i for i in range(1, 21)):
        sum += 2520
    print(sum)

if __name__ == '__main__':
    main()