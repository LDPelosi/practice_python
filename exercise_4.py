def divisor(n1):
    dividers = []
    for i in range(1, int(n1 / 2 + 1)):
        if n1 % i == 0:
            dividers.append(i)
    return dividers


def run():
    num = int(input('Choose a number: '))
    dividers = divisor(num)
    print(dividers)

if __name__ == '__main__':
    run()