import random

board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ]


player = "X"
comp = "O"


def display_board():
    """Displays the board"""
    for row in board:
        for item in row:
            print(" | ", item, " | ", end=" ")
        print()

def place_for_row(board):
    """Blocks the user from winning through row"""
    for row in range(len(board)):
        if board[row].count(player) == 2:
            if board[row][0] == player and board[row][1] == player and "-" in board[row]:
                board[row][2] = comp
                display_board()
                return
            elif board[row][0] == player and board[row][2] == player and "-" in board[row]:
                board[row][1] = comp
                display_board()
                return
            elif board[row][1] == player and board[row][2] == player and "-" in board[row]:
                board[row][0] = comp
                display_board()
                return


    return place_for_columns(board)

def place_for_columns(board):
    """Blocks the user from winning through column"""
    a = 0
    b = 0
    column_list = []
    while a <= 2:
            for row in range(0,3):
                column_list.append(board[row][b])
            a += 1
            b += 1
    
    

    if (column_list[0:3].count(player)) == 2 and "-" in column_list[0:3]:
        if column_list[0] == player and column_list[1] == player:
            board[2][0] = comp
            column_list.clear()
            display_board()
        elif column_list[0] == player and column_list[2] == player:
            board[1][0] = comp
            column_list.clear()
            display_board()
        elif column_list[1] == player and column_list[2] == player:
            board[0][0] = comp
            column_list.clear()
            display_board()


    elif (column_list[3:6].count(player)) == 2 and "-" in column_list[3:6]:
        if column_list[3] == player and column_list[4] == player:
            board[2][1] = comp
            column_list.clear()
            display_board()
        elif column_list[3] == player and column_list[5] == player:
            board[1][1] = comp
            column_list.clear()
            display_board()
        elif column_list[4] == player and column_list[5] == player:
            board[0][1] = comp
            column_list.clear()
            display_board()


    elif (column_list[6:9].count(player)) == 2 and "-" in column_list[6:9]:
        if column_list[6] == player and column_list[7] == player:
            board[2][2] = comp
            column_list.clear()
            display_board()
        elif column_list[6] == player and column_list[8] == player:
            board[1][2] = comp
            column_list.clear()
            display_board()
        elif column_list[7] == player and column_list[8] == player:
            board[0][2] = comp
            column_list.clear()
            display_board()


    else:
        column_list.clear()
        return place_for_diagnols(board)

def place_for_diagnols(board):
    """Blocks the user from winning through diagnols"""

    c = 0
    d = 0 
    diagonal_list = []

    while c <= 2:
        diagonal_list.append(board[c][d])
        c += 1
        d += 1
    

    e = 0
    f = 2

    while e <= 2:
        diagonal_list.append(board[e][f])
        e += 1
        f -= 1


    if diagonal_list[0:3].count(player) == 2 and "-" in diagonal_list[0:3]:
        if diagonal_list[0] == player and diagonal_list[1] == player:
            board[2][2] = comp
            diagonal_list.clear()
            display_board()
        elif diagonal_list[0] == player and diagonal_list[2] == player:
            board[1][1] = comp
            diagonal_list.clear()
            display_board()
        elif diagonal_list[1] == player and diagonal_list[2] == player:
            board[0][0] = comp
            diagonal_list.clear()
            display_board()

    elif diagonal_list[3:6].count(player) == 2 and "-" in diagonal_list[3:6]:
        if diagonal_list[3] == player and diagonal_list[4] == player:
            board[2][0] = comp
            diagonal_list.clear()
            display_board()
        elif diagonal_list[3] == player and diagonal_list[5] == player:
            board[1][1] = comp
            diagonal_list.clear()
            display_board()
        elif diagonal_list[4] == player and diagonal_list[5] == player:
            board[0][2] = comp
            diagonal_list.clear()
            display_board()
    else:
        diagonal_list.clear()
        return place_randomly(board)

def place_randomly(board):
    """Places randomly"""

    computer_row_num = random.randint(0,2)
    computer_column_num = random.randint(0,2)


    while board[computer_row_num][computer_column_num] != "-":
        computer_row_num = random.randint(0,2)
        computer_column_num = random.randint(0,2)
 
    board[computer_row_num][computer_column_num] = comp
    display_board()

def check_for_rows(board):
    """checks if someone won through row"""
    for row in range(len(board)):
        if (board[row][0] == player and board[row][1] == player and board[row][2] == player) or (board[row][0] == comp and board[row][1] == comp and board[row][2] == comp):
            print("You Won!!")
            return True

def check_for_columns(board):
    c_list = []
    x = 0
    y = 0
    while x <= 2:
            for row in range(0,3):
                c_list.append(board[row][y])        
            x += 1
            y += 1
        
    if (c_list[0] == player and c_list[1] == player and c_list[2] == player) or c_list[0] == comp and c_list[1] == comp and c_list[2] == comp:
            print("You Won :)")
            return True
    elif (c_list[3] == player and c_list[4] == player and c_list[5] == player) or c_list[3] == comp and c_list[4] == comp and c_list[5] == comp:
            print("You Won :)")
            return True
    elif (c_list[6] == player and c_list[7] == player and c_list[8] == player) or c_list[6] == comp and c_list[7] == comp and c_list[8] == comp:
            print("You Won :)")
            return True


def check_for_diagonal(board):
    g = 0
    h = 0 
    d_list = []

    while g <= 2:
        d_list.append(board[g][h])
        g += 1
        h += 1
    

    i = 0
    j = 2

    while i <= 2:
        d_list.append(board[i][j])
        i += 1
        j -= 1


    if (d_list[0] == player and d_list[1] == player and d_list[2] == player) or d_list[0] == comp and d_list[1] == comp and d_list[2] == comp:
            print("You Won :)")
            return True
    elif (d_list[3] == player and d_list[4] == player and d_list[5] == player) or d_list[3] == comp and d_list[4] == comp and d_list[5] == comp:
            print('You won :)')
            return True




def check_for_tie(board):
    items_in_board = []
    for row in range(len(board)):
        items_in_board.extend(board[row])

    if items_in_board.count("-") == 0:
        print('TIE!')
        return True

    
def main():
    display_board()
    valid_entries = ['1','2','3']
    while True:
        print("Your Turn!")
        row_num = input("Enter which row you want to place it in: ")
        column_num = input("Enter which column you want to place it in: ")

        while row_num not in valid_entries or column_num not in valid_entries:
            print("Invalid Input")
            display_board()
            row_num = input("Enter which row you want to place it in: ")
            column_num = input("Enter which column you want to place it in: ")
        
        row_num, column_num = int(row_num) - 1, int(column_num) - 1

        try:
            while board[row_num][column_num] != "-":
                print("That spot has been taken. Choose a different spot.")
                display_board()
                row_num = int(input("Enter which row you want to place it in: ")) - 1
                column_num = int(input("Enter which column you want to place it in: ")) - 1

            board[row_num][column_num] = player
        except Exception as err:
            print('ERROR! Choose a different spot!')
            continue

        display_board()


        if check_for_rows(board) or check_for_columns(board) or check_for_diagonal(board) or check_for_tie(board):
            return

        print("Computer's turn!")
        place_for_row(board)







main()


