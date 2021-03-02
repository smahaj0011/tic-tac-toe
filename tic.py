board = [
            ["X","X","-"],
            ["X","O","-"],
            ["-","X","X"]
        ]


player = "X"
comp = "O"
column_list = []
run_column_fxn = ''

def display_board():
    for row in board:
        for item in row:
            print(" | " + item + " | ", end=" ")
        print()


def find_index(elements_list, key):
  result_list = []

  for x in range(len(elements_list)):
    if elements_list[x] == key:
      result_list.append(x)
  
  return result_list


def check_for_rows(board):
    for row in range(len(board)):
        for x in range(0,3):
            if board[row].count(player) == 2:
                row_repeating = board[row]
                print("Player is repeating in:",row_repeating)
                global index_num
                index_num = find_index(row_repeating, player)

                if (board[row][0] == player) and (board[row][1] == player):
                    board[row][2] = "O"
                    display_board()
                elif (board[row][0] == player) and (board[row][2] == player):
                    board[row][1] = "O"
                    display_board()
                elif (board[row][0] == player) and (board[row][2] == player):
                    board[row][0] = "O"
                    display_board()
                break
        break
    
        
def check_for_columns(board):
    x = 0
    y = 0
    while x <= 2:
            for row in range(0,3):
                # print("Item:",board[row][y]) 
                column_list.append(board[row][y])
                # print("list:",column_list)
            x += 1
            y += 1

    
    print("list:",column_list)
    global index_of_repeating
    if (column_list[0:3].count(player)) == 2:
        index_of_repeating = find_index(column_list[0:3], player)
        print("index_of_repeating1:",index_of_repeating)
        if column_list[0] == player and column_list[1] == player:
            board[2][0] = comp
            display_board()
        elif column_list[0] == player and column_list[2] == player:
            board[1][0] = comp
            display_board()
        elif column_list[1] == player and column_list[2] == player:
            board[0][0] = comp
            display_board()

    elif (column_list[3:6].count(player)) == 2:
        index_of_repeating = find_index(column_list[3:6], player)
        print("index_of_repeating2:",index_of_repeating)
        if column_list[3] == player and column_list[4] == player:
            board[2][1] = comp
            display_board()
        elif column_list[3] == player and column_list[5] == player:
            board[1][1] = comp
            display_board()
        elif column_list[4] == player and column_list[5] == player:
            board[0][1] = comp
            display_board()


    elif (column_list[6:9].count(player)) == 2:
        index_of_repeating = find_index(column_list[6:9], player)
        print(column_list[6:9])
        print("index_of_repeating3:",index_of_repeating)
        if column_list[6] == player and column_list[7] == player:
            board[2][2] = comp
            display_board()
        elif column_list[6] == player and column_list[8] == player:
            board[1][2] = comp
            display_board()
        elif column_list[7] == player and column_list[8] == player:
            board[0][2] = comp
            display_board()
    
    else:
        c = random.randint(0,2)
        d = random.randint(0,2)


        while board[c][d] != "-":
            c = random.randint(0,2)
            d = random.randint(0,2)
        else:
            board[c][d] = "O"
        

    


# def check_for_diagnols(board):


def main():
  valid_entries = [0,1,2]
  while True:

    print("Your turn")
    a = int(input("enter row num: "))
    b = int(input("enter column num: "))

    try:
      while board[a][b] != "-":
          print("invalid")
          a = int(input("enter num: "))
          b = int(input("enter num again: "))
      board[a][b] = "X"
    
    except:
      print('umm, please enter a number between 1-9')
      continue

    for row in board:
      for item in row:
        print(" | " + item + " | ", end=" ")
      print()

    print("Computer's turn")

    c = random.randint(0,2)
    d = random.randint(0,2)


    while board[c][d] != "-":
      c = random.randint(0,2)
      d = random.randint(0,2)
      print(c,d)
    else:
      board[c][d] = "O"

      for row in board:
        for item in row:
          print(" | " + item + " | ", end=" ")
        print()


display_board()
# check_for_columns(board)
check_for_rows(board)
if run_column_fxn != False:
    check_for_columns(board)
    run_column_fxn = ''
print(board)



# display_board()



# print(index_of_repeating)
# print("Index_num:",index_num)
# print("column list:",column_list)





