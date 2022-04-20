import random as r

def run():
    num = r.randint(1, 9)
    
    while True:
        chosen = int(input("Choose a number between 1 and 9: "))
        if chosen < num:
            print("The numbers is higher")
        elif chosen > num:
            print("The number is lower")
        
        if num == chosen:
            print(f"Well done! the number is {chosen}")
            break



if __name__ == '__main__':
    run()