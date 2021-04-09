def main():
    i1, i2 = 1, 1
    sum = 0
    while i1 < 4_000_000:
        if i1 % 2 == 0:
            sum += i1
        i1, i2 = i1 + i2, i1
    print(sum)

if __name__ == '__main__':
    main()