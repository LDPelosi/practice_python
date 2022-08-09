def make_messeje(func):
    def wrapper(*args, **kwargs):
        print(f'This is the list')
        func(*args, **kwargs)
    return wrapper


@make_messeje
def run():
    a = [1, 3, 5, 8]
    b = [1, 3, 9, 4]

    c = [num for num in b if num in a] 
    print(c)


if __name__ == '__main__':
    run()