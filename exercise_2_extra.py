def run():
    num = int(input("Enter a number: "))
    check = int(input("Enter a second number: "))
    if num % check == 0:
        print(f'{num} and {check} is divided evenly')
    else:
        print(f'{num} and {check} dont´t divided evenly')


if __name__ == '__main__':
    run()