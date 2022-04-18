import random

def player_win(opt1, opt2):
    if (opt1 == 'rock' and opt2 == 'scissors') or (opt1 == 'paper' and opt2 == 'rock') or (opt1 == 'scissors' and opt2 == 'paper'):
        return True
    else:
        return False

def run():
    hi = """
        Hi this is a rock, paper, scissors game please choose:

        Rock
        Paper
        Scissors
    
    """
    options = ['rock', 'paper', 'scissors']
    play = 'y'

    while True:
        if play == 'n':
            break
        else:
            print(hi)
            player_choice = (input('your choice: ')).lower()
            computer_choice = random.choice(options)
            
            if player_choice == computer_choice:
                print(f'You chose {player_choice} and the computer chose {computer_choice}, ITS A TIDE!!!')
            elif player_win(player_choice, computer_choice):
                print(f'You chose {player_choice} and the computer chose {computer_choice}, YOU WIN!!!')
            else:
                print(f'You chose {player_choice} and the computer chose {computer_choice}, YOU LOST!!!')

            play = input('if you want play again plase tip "y" else tip "n" : ').lower()


if __name__ == '__main__':
    run()