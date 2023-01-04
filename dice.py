import random


ROLL = 0
WIN_TOTAL = 0
LOSS_TOTAL = 0


dice_1 =    """
             -------
            |       |
            |   x   |
            |       |
             -------"""

dice_2 = """ 
             -------
            | x     |
            |       |
            |     x |
             -------"""

dice_3 = """
             -------
            | x     |
            |   x   |
            |     x |
             -------"""

dice_4 = """ 
             -------
            | x   x |
            |       |
            | x   x |
             -------"""

dice_5 = """ 
             -------
            | x   x |
            |   x   |
            | x   x |
             -------"""

dice_6 = """ 
             -------
            | x   x |
            | x   x |
            | x   x |
             -------"""



def winning_move(dice1, dice2):
    if dice1 + dice2 in [7, 11]:
        return True


def losing_move(dice1, dice2):
    if dice1 + dice2 in [2, 3, 12]:
        return True

def print_dice(dice1, dice2):
    if dice1 == 1:
        dice1 = dice_1
    elif dice1 == 2:
        dice1 = dice_2
    elif dice1 == 3:
        dice1 = dice_3
    elif dice1 == 4:
        dice1 = dice_4
    elif dice1 == 5:
        dice1 = dice_5
    elif dice1 == 6:
        dice1 = dice_6

    if dice2 == 1:
        dice2 = dice_1
    elif dice2 == 2:
        dice2 = dice_2
    elif dice2 == 3:
        dice2 = dice_3
    elif dice2 == 4:
        dice2 = dice_4
    elif dice2 == 5:
        dice2 = dice_5
    elif dice2 == 6:
        dice2 = dice_6

    print(dice1, dice2)



playing = True

while playing:

    print('\n')
    ask_for_roll = input("Type 'R' to ROLL. 'Q' to quit: ").lower()
    

    try:
        if ask_for_roll == 'r':

            ROLL += 1

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            dice_total = dice1 + dice2
            print(f'Dice1: {dice1}, Dice2: {dice2} \t Total: {dice_total}')
            print_dice(dice1, dice2)
            

            winning_move(dice1, dice2)
            losing_move(dice1, dice2)

            if losing_move(dice1, dice2):
                LOSS_TOTAL += 1
                print('\t You Lose \n')

                play_again = input("\t Do you wish to play again? 'y' for yes, 'n' for no. ").lower()
                if play_again == 'y':
                    continue
                else:
                    break
                        
            if winning_move(dice1, dice2):
                WIN_TOTAL += 1
                print('\t You Win \n')

                play_again = input("\t Do you wish to play again? 'y' for yes, 'n' for no. ").lower()
                if play_again == 'y':
                    continue
                else:
                    break


        elif ask_for_roll == 'q':
            break
    except:
        print("Please type in 'R' to ROLL or 'Q' to quit: ")


print(f'\n \t YOU WON {WIN_TOTAL} TIMES, LOST {LOSS_TOTAL} TIMES \n')

