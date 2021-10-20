import datetime

def run():
    num = int(input("How many times you want repeat this?: "))
    name = input("What´s your name?: ")
    age = int(input("How old are you? "))
    actual_year = datetime.datetime.now()
    diference = 100 - age
    year_hundred = actual_year.year + diference

    
    print(num *  f'Hi {name} in the year {year_hundred} you will have 100 years old \n')
    




if __name__ == '__main__':
    run()