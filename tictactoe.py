from minmaxtictactoe import minmax

class tictactoe:

    def __init__(self):
 
        self.reset_board()

    def reset_board(self):

        self.x_map = [[False,False,False],[False,False,False],[False,False,False]]
        self.o_map = [[False,False,False],[False,False,False],[False,False,False]]


    def make_move(self, player, row, col):

        if (row>3 or row<1) or (row>3 or row<1):
            print("Dimensions out of range, pls enter between 1 and 3.")
            return False
        
        row = row-1
        col = col-1

        if self.x_map[row][col] == True or self.o_map[row][col] == True:
            print("There is already a piece there.")
            return False

        if player == 0:
            self.x_map[row][col] = True
        else:
            self.o_map[row][col] = True
        
        return True


        
    def show_board(self):
        #todo: make it friendly to this class

        whole = []
        for i, (x_row, o_row) in enumerate(zip(self.x_map, self.o_map)):
            line = ""    
            for k, (x_col, o_col) in enumerate(zip(x_row, o_row)):
                
                if x_col == True:
                    line += "X"
                elif o_col == True:
                    line += "O"
                else:
                    line += " "

                if k<2:
                    line += "|"
            
            whole.append(line)
            if i<2:
                whole.append("-----")

        print("\n".join(whole))


    def check_win(self):
            
        for x_row, o_row in zip(self.x_map, self.o_map):
            if all(x_row):
                return (1 ,True)
            elif all(o_row):
                return (-1, True)

        transposed_x = [list(i) for i in zip(*self.x_map)]
        transposed_y = [list(i) for i in zip(*self.o_map)]
        for x_row, o_row in zip(transposed_x, transposed_y):
            if all(x_row):
                return (1, True)
            elif all(o_row):
                return (-1, True)
        
        
        if all([row[i] for i,row in enumerate(self.x_map)]) or all([row[-i-1] for i,row in enumerate(self.x_map)]):
            return (1, True)
        elif all([row[i] for i,row in enumerate(self.o_map)]) or all([row[-i-1] for i,row in enumerate(self.o_map)]):
            return (-1, True)

        control_list = []
        for x_row, o_row in zip(self.x_map, self.o_map):
            for x_col, o_col in zip(x_row, o_row):
                control_list.append(x_col or o_col)
        
        if all(control_list):
            
            return (0, True)

        return (0, False) 


    def get_board(self):
        return (self.x_map, self.o_map)


game = tictactoe()

finished = False
while not finished:
    player_move = [int(x) for x in input("your turn:").split(",")]
    print(player_move)
    game.make_move(1, *player_move)
    game.show_board()
    status,terminal = game.check_win()
    if status == 1:
        finished = True
        print("X Won!")
        break
    elif status == -1:
        finished = True
        print("O Won!")
        break
    elif status == 0 and terminal:
        finished = True
        print("Draw!")
        break

    ai_move = [x+1 for x in minmax(*game.get_board(),True)]
    print(ai_move)
    game.make_move(0, *ai_move)
    game.show_board()
    status,terminal = game.check_win()
    if status == 1:
        finished = True
        print("X Won!")
        break
    elif status == -1:
        finished = True
        print("O Won!")
        break
    elif status == 0 and terminal:
        finished = True
        print("Draw!")
        break
