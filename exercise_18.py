import random
def generate_random_num():
    r_num = ""

    for i in range(4):
        num = str(random.randint(0,9))
        r_num = r_num + num
        
    return r_num

def run():
    attempts = 0
    r_num = generate_random_num()
    print(r_num)
    while True:
        cows = 0
        bullets = 0
        attempts += 1
        player_num = input('Choose a 4 digit number: ')
        try:
           for i in range(len(player_num)):
                    if player_num[i] == r_num[i]:
                        cows += 1
                    if player_num[i] in r_num:
                        bullets += 1     
        except:
            print("Please enter a 4 digit number")
            continue
        print(f'COWS: {cows}  BULLETS: {bullets}')
        
    
        if player_num == r_num:
            print(f'You guessed the number and only take you {attempts} attempts')
            break
    
if __name__ == '__main__':
    run()