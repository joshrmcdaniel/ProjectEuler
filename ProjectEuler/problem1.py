def main():
    total = sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])
    print(total)


if __name__ == '__main__':
    main()
