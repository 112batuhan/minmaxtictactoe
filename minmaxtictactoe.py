import copy

def check_win(board_x, board_o):
    for x_row, o_row in zip(board_x, board_o):
        if all(x_row):
            return (1 ,True)
        elif all(o_row):
            return (-1, True)

    transposed_x = [list(i) for i in zip(*board_x)]
    transposed_y = [list(i) for i in zip(*board_o)]
    for x_row, o_row in zip(transposed_x, transposed_y):
        if all(x_row):
            return (1, True)
        elif all(o_row):
            return (-1, True)
    
    
    if all([row[i] for i,row in enumerate(board_x)]) or all([row[-i-1] for i,row in enumerate(board_x)]):
        return (1, True)
    elif all([row[i] for i,row in enumerate(board_o)]) or all([row[-i-1] for i,row in enumerate(board_o)]):
        return (-1, True)

    control_list = []
    for x_row, o_row in zip(board_x, board_o):
        for x_col, o_col in zip(x_row, o_row):
            control_list.append(x_col or o_col)
    
    if all(control_list):
        return (0, True)

    return (0, False)

count = 0

def max_value(board_x,board_o):
    global count
    count +=1
    result, terminate = check_win(board_x, board_o)
    if terminate: 
        return result
        
    v = -10000
    i=0
    while(i<3):
        k=0
        while(k<3):
            if board_x[i][k] != True and board_o[i][k] != True:
                new_board_x = copy.deepcopy(board_x)
                new_board_o = copy.deepcopy(board_o)
                new_board_x[i][k] = True
                v = max(v, min_value(new_board_x, new_board_o))
            k += 1
        i += 1
                
    return v

def min_value(board_x, board_o):
    global count
    count +=1
    result, terminate = check_win(board_x, board_o)
    if terminate: 
        return result
    
    v = 10000
    m=0
    while(m<3):
        n=0
        while(n<3):
            if board_x[m][n] != True and board_o[m][n] != True:
                new_board_x = copy.deepcopy(board_x)
                new_board_o = copy.deepcopy(board_o)
                new_board_o[m][n] = True
                v = min(v, max_value(new_board_x, new_board_o))
            n += 1
        m += 1

    return v



count_ab = 0

def max_value_ab(board_x,board_o, alpha, beta):
    global count_ab
    count_ab +=1
    result, terminate = check_win(board_x, board_o)
    if terminate: 
        return result
        
    v = -10000
    i=0
    while(i<3):
        k=0
        while(k<3):
            if board_x[i][k] != True and board_o[i][k] != True:
                new_board_x = copy.deepcopy(board_x)
                new_board_o = copy.deepcopy(board_o)
                new_board_x[i][k] = True
                v = max(v, min_value_ab(new_board_x, new_board_o, alpha, beta))
                if (v >= beta): 
                    return v
                alpha = max(alpha, v)

            k += 1
        i += 1
                
    return v

def min_value_ab(board_x, board_o, alpha, beta):
    global count_ab
    count_ab +=1
    result, terminate = check_win(board_x, board_o)
    if terminate: 
        return result
    
    v = 10000
    i=0
    while(i<3):
        k=0
        while(k<3):
            if board_x[i][k] != True and board_o[i][k] != True:
                new_board_x = copy.deepcopy(board_x)
                new_board_o = copy.deepcopy(board_o)
                new_board_o[i][k] = True
                v = min(v, max_value_ab(new_board_x, new_board_o, alpha, beta))
                if (v <= alpha): 
                    return v
                beta = min(beta, v)

            k += 1
        i += 1

    return v


def minmax(board_x, board_o, ab = False):
    
    (val, action) = (-10000, None)
    i=0
    while(i<3):
        k=0
        while(k<3):
            if board_x[i][k] != True and board_o[i][k] != True:
                new_board_x = copy.deepcopy(board_x)
                new_board_o = copy.deepcopy(board_o)
                new_board_x[i][k] = True

                if ab:
                    v = min_value_ab(new_board_x, new_board_o, -10000, 10000)
                else:
                    v = min_value(new_board_x, new_board_o)

                if  val <= v:
                   (val, action) = (v, (i,k))
            k += 1
        i += 1
    return action


#board_x = [[False,False,False],[False,False,False],[False,False,False]]
#board_o = [[False,False,False],[False,False,False],[False,False,False]]

#max_value(board_x, board_o)
#max_value_ab(board_x, board_o, -10000, 10000)
#print(count, count_ab, count/count_ab)

#print(minmax(board_x,board_o, True))