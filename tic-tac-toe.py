#tasks
#create board
#check for win and draw
#change turns
#place pieces

# in case of future need
#ROW1 = board[0] == board[1] == board[2]
#ROW2 = board[3] == board[4] == board[5]
#ROW3 = board[6] == board[7] == board[8]
#COLUMN1 = board[0] == board[3] == board[6]
#COLUMN2 = board[1] == board[4] == board[7]
#COLUMN3 = board[2] == board[5] == board[8]
#ACROSS1 = board[0] == board[4] == board[8]
#ACROSS2 = board[6] == board[4] == board[2]
#all = ROW1 + ROW2 + ROW3 + COLUMN1 + COLUMN2 + COLUMN3 + ACROSS1 + ACROSS2



WIN = False

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_win():
    #check rows for X
    if board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or board[6] == board[7] == board[8] == "X":
        WIN = True
        print("Player 1 wins")
        quit()
    #check rows for O
    if board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or board[6] == board[7] == board[8] == "O":
        WIN = True
        print("Player 2 wins")
        quit()

    #check columns for X
    if  board[0] == board[3] == board[6] == "X" or board[1] == board[4] == board[7] == "X" or board[2] == board[5] == board[8] == "X":
        WIN = True
        print("Player 1 wins")
        quit()
    #check columns for O
    if  board[0] == board[3] == board[6] == "O" or board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O":
        WIN = True
        print("Player 2 wins")
        quit()

    #check across for X
    if board[0] == board[4] == board[8] == "X" or board[6] == board[4] == board[2] == "X":
        WIN = True
        print("Player 1 wins")
        quit()
    #check across for O
    if board[0] == board[4] == board[8] == "O" or board[6] == board[4] == board[2] == "O":
        WIN = True
        print("Player 2 wins")
        quit()


#check draw
def check_for_draw():
    if "-" not in board and WIN != True:
        print("Tie")
        quit()


playing = True

while playing:

    display_board()

    turn = 1

    num_list = list(range(1, 10))
    nums = str(num_list)

    #player 1 turn 
    while turn == 1:         
        position = input("Player 1 choose a position from 1 - 9: ")

        if position in nums:
            position = int(position) - 1   
        else:
            print("please type a number from 1-9")
            continue
        
        if position > 8:
            print("please type a number from 1-9")  
            continue  
        elif board[position] != "-":           
            continue     
        elif position <= 8:           
            board[position] = "X"           
            turn += 1       
            display_board()           
            check_win()           
            check_for_draw()       
        else:           
            print("Something wrong, try again")           
            continue   

    #player 2 turn  
    while turn == 2:       
        position = input("Player 2 choose a position from 1 - 9: ")

        if position in nums:
            position = int(position) - 1   
        else:
            print("please type a number from 1-9")
            continue

        if position > 8:
            print("please type a number from 1-9")  
            continue       
        elif board[position] != "-":           
            continue
        elif position <= 8:           
            board[position] = "O"           
            turn -= 1           
            display_board()           
            check_win()           
            check_for_draw()       
        else:           
            print("Something wrong, try again")
            continue