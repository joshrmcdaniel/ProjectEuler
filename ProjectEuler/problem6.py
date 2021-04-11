def main():
    rang3 = range(1, 101)
    sum1 = sum(i ** 2 for i in rang3)
    sum2 = sum(i for i in rang3) ** 2
    print(sum2 - sum1)

if __name__ == '__main__':
    main()