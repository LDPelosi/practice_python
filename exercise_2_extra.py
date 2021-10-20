def run():
    num = int(input("Enter a number: "))
    check = int(input("Enter a second number: "))
    if num % check == 0:
        print(f'{num} divides evenly by {check}')
    else:
        print(f'{num} doesn´t diveds evenly by {check} ')


if __name__ == '__main__':
    run()