def divisor(n1):
    dividers = []
    try:
        if n1 < 0:
            raise ValueError('Negative numbers are not valid')
        for i in range(1, int(n1 / 2 + 1)):
            if n1 % i == 0:
                dividers.append(i)
        return dividers
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input('Choose a number: '))
        dividers = divisor(num)
        print(dividers)
    except ValueError:
        print('Value is not valid')
if __name__ == '__main__':
    run()