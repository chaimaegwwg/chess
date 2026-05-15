from game import render,ft_boerd
import sys

#mission is make rule for the bishop  blackkkkkkkkkk

#pawn pass the finale one | i will take it to the final
# after the pawn there is the 


class Step:
    def __init__(self, col, row,value):
        self.visited = 0
        self.col = col
        self.row = row
        self.value = value   


def inside_class():
    boerd = ft_boerd()
    steps_grid = []
    for x in range(8):
        row_list = []
        for y in range(8):
            step = Step(x,y,boerd[x][y])
            row_list.append(step)
        steps_grid.append(row_list)
    return steps_grid


def ft_position(from_p, boerd):
    for row in range(8):
        for col in range(8):
            if boerd[row][col] == from_p:
                return (row, col)
    return (0,0)


def rule_move_pawn_white(from_p, to , boerd,grid):
    from_row , from_col = ft_position(from_p, boerd)
    to_row , to_col = ft_position(to, boerd)
    opponent = ['p','r','b','q','n']

    distance = from_row - to_row 
    try:
        if from_row < to_row:
            raise ValueError("you can't move to down")
        elif from_col != to_col:
            current = to.split(":")
            previos = from_p.split(":")
            if (to_col == from_col+1 or to_col == from_col -1) and current[1] in opponent:
                print("i enter :        ")
                grid[from_row][from_col].value = previos[0]+":"+"#"
                boerd[from_row][from_col] = grid[from_row][from_col].value
            else:
                raise ValueError("you can't move only front not on the side")

        elif distance > 2:
            raise ValueError("extra step")
        elif grid[from_row][from_col].visited > 0 and distance > 1:
            raise ValueError("extra step")
        if grid[from_row][from_col].visited == 0:
            grid[to_row][to_col].visited += 1       
    
    except ValueError as e:
        print("Error:", e)
        return False
    return True

def rule_move_pawn_black(from_p, to, boerd, grid):
    from_row , from_col = ft_position(from_p, boerd)
    to_row , to_col = ft_position(to, boerd)
    opponent = ['P','R','B','Q','N']
    distance = to_row - from_row 
    try:
        if from_row > to_row:
            raise ValueError("you can't move to down black")
        elif from_col != to_col:
            current = to.split(":")
            previos = from_p.split(":")
            if (to_col == from_col+1 or to_col == from_col -1) and current[1] in opponent:
                grid[from_row][from_col].value = previos[0]+":"+"#"
                boerd[from_row][from_col] = grid[from_row][from_col].value
            else:
                raise ValueError("you can't move only front not on the side")
        elif distance > 2:
            raise ValueError("extra step for black")
        elif grid[from_row][from_col].visited > 0 and distance > 1:
            raise ValueError("extra step for black")
        if grid[from_row][from_col].visited == 0:
            grid[to_row][to_col].visited += 1       
    
    except ValueError as e:
        print("Error:", e)
        return False
    return True


def move_generale(first, second,fro_m, to, boerd):
    fro_m = first.split(":")
    to = second.split(":")
    temp = fro_m[1]
    for row in range(8):
        for i in range(8):
            if boerd[row][i] == first:
                boerd[row][i] = str(fro_m[0]+":"+to[1])
            elif boerd[row][i] == second:
                boerd[row][i] = str(to[0]+":"+temp)
    return boerd


def must_be_white(first):
    character = first.split(":")
    character = character[1].strip()
    if character == "P":
        return True
    elif character == "B":
        return True
    elif character == "N":
        return True
    elif character == "Q":
        return True
    elif character == "R":
        return
    elif character == "K":
        return True
    else:
        return False


def must_be_black(first):
    character = first.split(":")
    character = character[1].strip()
    if character == "p":
        return True
    elif character == "b":
        return True
    elif character == "n":
        return True
    elif character == "q":
        return True
    elif character == "r":
        return
    elif character == "k":
        return True
    else:
        return False
#check the bishop
def check_bishop(from_p , to, boerd, grid):
    character = from_p.split(":")
    oppon = to.split(":")
    friendly = ['B','#']
    opponent = ['p','r','b','q','n']
    mine = ['R','N','B','Q','K']
    from_row, from_col = ft_position(from_p,boerd)
    to_row, to_col = ft_position(to,boerd)
    f_r = from_row
    f_c = from_col
    go_to = abs(from_row - to_row)
    
    try:
        if abs(from_row - to_row) != abs(from_col - to_col):
            raise ValueError("please move the bishop so form like x")
        right_left = from_col - to_col
        up_down = from_row - to_row
        if right_left < 0 and up_down < 0:
            direction = "right_down"
        elif right_left > 0 and up_down < 0:
            direction = "left_down"
        elif right_left < 0 and up_down > 0:
            direction = "right_up"
        elif right_left > 0 and up_down > 0:
            direction = "left_up"
        if right_left == 0 and up_down == 0:
            return False
        while True:
            if direction == "left_up":
                from_row -= 1
                from_col -= 1
            elif direction == "right_up":
                from_row -= 1
                from_col += 1
            elif direction == "left_down":
                from_row += 1
                from_col += 1
            elif direction == "right_down":
                from_row += 1
                from_col -= 1
            value = boerd[from_row][from_col].split(":")
            if value[1] not in friendly and not from_col == to_col:
                raise ValueError("you can't jump hhhh u are not Knight")
            if (from_col == to_col or from_row == to_row) and value[1] in mine:
                raise ValueError("you can't jump hhhh u are not Knight")
                break
            if from_col == to_col or from_row == to_row:
                break
            
        if oppon[1] in opponent:
            grid[f_r][f_c].value = character[0]+":"+"#"
            boerd[f_r][f_c] = grid[f_r][f_c].value
    except ValueError as e:
        print("Error", e)
        return False
    return True
    

def rule_rock(fro_m, to, boerd, grid):
    from_row, from_col = ft_position(from_p,boerd)
    to_row, to_col = ft_position(to,boerd)
    try:
        if from_col != to_col:
            raise ValueError("you can't move diagonal")
        # if to
        




    except ValueError as e:
        print("Error",e)
        return False
    return True


def check_and_move(first, second,peace, boerd,grid,turn):
    fro_m = first
    to = second
    if peace == "P":
        check_move = rule_move_pawn_white(fro_m, to, boerd, grid)
    elif peace == "B" or peace == "b":
        check_move = check_bishop(fro_m , to, boerd, grid)
    elif peace == "R":
        check_move = rule_rock(fro_m, to, boerd, grid)
 

    if turn == "white":
        if check_move:
            boerd = move_generale(first, second,fro_m, to, boerd)
            render(boerd)
            return True
        else:
            return False
    else:
        if peace == "p":
            check_move = rule_move_pawn_black(fro_m, to, boerd, grid)
        elif peace == "B" or peace == "b":
            check_move = check_bishop(fro_m , to, boerd, grid)
        eif peace == "r":
        check_move = rule_rock(fro_m, to, boerd, grid)

        if check_move:
            boerd = move_generale(first, second,fro_m, to, boerd)
            render(boerd)
            return True
        else:
            return False

def move_generale_from_to():
    grid = inside_class()
    boerd = ft_boerd()
    render(boerd)
    check = 1
    trun ="white"
    while True:
        try:
            first = str(input("\033[90mPlease entery the peace that u want to move it from: "))
            if first == "exit":
                sys.exit()
            second = str(input("Please entery the peace that u want to move it to : "))
            if second == "exit":
                sys.exit()
        except:
            sys.exit()
        if not any(first in row for row in boerd):
            print('\033[93m',"==> please enter the place of this peace",'\033[0m')
            print('\033[91m',"if u want to end the game just enter: exit",'\033[0m')
            continue
        if first == "exit" or second == "exit":
            sys.exit()
        x_fr = first.split(":")
        if trun == "white":
            if must_be_white(first):
                if not check_and_move(first, second, x_fr[1],boerd,grid,trun):
                    trun = "white"
                    continue
                trun = "black"
            else:
                print("this must be the turn of white")
                trun = "white"
                continue
        elif trun == "black":
            if must_be_black(first):
                if not check_and_move(first, second, x_fr[1], boerd,grid,trun):
                    trun = "black"
                    continue
                trun = "white"
            else:
                print("this must be the turn of black")
                trun = "black"
                continue

move_generale_from_to()
