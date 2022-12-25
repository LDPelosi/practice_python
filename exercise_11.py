def prime(num):
    result = True
    if num == 1:
        result = False
    else: 
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
            else:
                result = True
    return result

def run():
    num = int(input("Give me a number: "))
    if prime(num):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

if __name__ == '__main__':
    run()