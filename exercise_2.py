def run():
    num = int(input("Enter a number: "))
    if num % 4 == 0:
        print(f'The number {num} is multiplie of 4 and even')
    elif num % 2 == 0:
        print(f'The number {num} is even')
    else:
        print(f'The number {num} is odd')


if __name__ == '__main__':
    run()