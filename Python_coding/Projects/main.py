def display_game(board):
    j = 0
    for i in range(0,3):
        print(board[j] + "  |  " + board[j+1] + " | " + board[j+2])
        if i != 2:
            print("------------")
        j += 3

def check_winning(board, marker,turns):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] \
    or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] \
    or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return 0
    if turns == 9:
        return 1
    else:
        return 2

def user_input(board,turns):
    marker = input("please enter a your sign 'X' or 'O': ")
    if marker != 'X' and marker != 'O':
        print("invalid value, please follow as mentioned")
        user_input(board)
    location = int(input("enter the location: ")) - 1
    if location < 0 or location > 8:
        print("invalid value, please follow as mentioned")
        user_input(board)
    if board[location] == 'X' or  board[location] == 'O':
        print("this place already taken")
        user_input(board,turns)
    turns += 1
    board[location] = marker
    display_game(board)
    won = check_winning(board, marker,turns)
    if won == 0:
        print("player - " + marker + " has won the game!")
        quit() # own of the players has won thus we end the game
    if won == 1:
        print("its a tie!")
        quit()
    user_input(board,turns)




def main():
    turns = 0
    board = ["1","2","3","4","5","6","7","8","9",]
    display_game(board)
    user_input(board,turns)

if __name__ == "__main__":
    # execute only if run as a script
    main()