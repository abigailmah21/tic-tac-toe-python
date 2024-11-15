
# Tic-Tac-Toe Game in Python


print('Welcome to Tic Tac Toe! To win, you should obtain a straight line of your letter(Either vertical, horizontal or diagonal).\n')

# This displays the reference for the 9 choices of positions.
print(20*' ',"   reference:    ")
print(20*' ','     |    |      ') 
print(20*' ','  1  | 2  | 3    ')
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  4  | 5  | 6    ")
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  7  | 8  | 9    \n")


def display_board(): # This function displays the game board.
    print()
    print('     |    |     ',10*' ','     |    |   ',)
    print('  '+board[1]+'  | '+board[2]+'  | '+board[3]+'   ',10*' ','  1  | 2  | 3  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |     ")
    print('  '+board[4]+'  | '+board[5]+'  | '+board[6]+'   ',10*' ',"  4  | 5  | 6   ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |      ")
    print('  '+board[7]+'  | '+board[8]+'  | '+board[9]+'   ',10*' ',"  7  | 8  | 9    \n\n")


def human_input(piece): # Human player's turn
    while True:
        inp = input(f"[Human] '{piece}' Enter your move (1-9): ")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[Human] '{piece}' This position is already occupied.")
        else:
            print(f"[Human] '{piece}' Please enter a valid option (1-9)!")


def winning(piece,board): 
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] # Total of 8 possible winning arrangements.
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == piece:
            return True


def win_move(i,board,piece):
    temp_board = list(board)
    temp_board[i] = piece
    if winning(piece,temp_board):
        return True
    else:
        return False


def computer_input(computer , human , board): # Computer's turn.
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,computer):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,human):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i


def new_game(): # This function asks player if they want to continue a new game.
    while True:
        nxt = input('[Human] Do you want to play again?(y/n):')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print('Thank you for playing!')
            again = False
            break
        else:
            print('Enter correct input (y/n)!')
    if again:
        print('__________NEW GAME__________')
        main_game()
    else:
        return False

 
def win_check(human , computer): 
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('[Human] wins the game!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == computer:
                print('[Computer] wins the game!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('Tie game!')
        if not new_game():
            return False
    return True


def user_choice(): # Let's the player choose which piece they want to be.
    while True:
        inp = input('[Human]Choose your piece [x/o]: ')
        if inp in ['x' , 'X']: # Human player plays first if 'x' is chosen.
            print('[Human]You chose "X".\n[Human]You play first!')
            return 'x','o'
        elif inp in ['O','o']: # Computer plays first if player choosen 'o'.
            print('[Human] You chose "O".\n[Human] Computer plays first.')
            return 'o','x'
        else:
            print('[Human] Enter correct input! [x/o]')


def main_game():
    global board
    play = True
    board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    human , computer = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human , computer)
            if play:
                o = computer_input(computer , human , board)
                print(f"[Computer] Entered:{o}")
                board[o] = computer
                display_board()
                play = win_check(human , computer)
        else:
            x = computer_input(computer , human , board)
            print(f"[Computer] Entered: {x}")
            board[x] = computer
            display_board()
            play = win_check(human , computer)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human , computer)

           
if __name__ == '__main__':
    main_game()
        
