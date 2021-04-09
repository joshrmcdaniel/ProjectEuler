def main():
    palindrones = []

    for i in range (100, 1000):
        for j in range(100, i):
            product = str(i * j)
            if product == product[::-1]:
                palindrones.append(product)

    palindrones = map(int, palindrones)
    print(max(palindrones))


if __name__ == '__main__':
    main()
