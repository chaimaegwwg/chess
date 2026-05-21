from game import render,ft_boerd
import sys
#problem the king swap not eat 
#the mission and the finale is to check also checkmate 

#pawn pass the finale one | i will take it to the final
#pawn on the finale can transfert to any thing he wanted
# move make sure the black have the same move of the white to finish 
 
#mission a square between the kings

#the mission is the # can't move check this 

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
    lst = ["P","B","N","Q","R","K"]
    return character in lst

def must_be_black(first):
    character = first.split(":")
    character = character[1].strip()
    lst = ["p","b","n","q","r","k"]
    return character in lst




def rule_checks(from_c, to, boerd, grid):
    pass



def rule_king(from_k, to, boerd, grid):
    from_col ,from_row = ft_position(from_k,boerd)
    to_col ,to_row = ft_position(to,boerd)
    char = grid[from_col][from_row].value
    char = char.split(":")
    charac = from_k.split(":")
    dx = to_row - from_row
    dy = to_col - from_col

    opponent = ['p','r','b','q','n']
    oppon = to.split(":")
    
    character = to.split(":")
    mine = ['R','N','B','Q','P']
    lst = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
 
    try:
        if not tuple(sorted((abs(dx),abs(dy)))) in [(1,1), (0, 1)]:
            raise ValueError("you are king be wise remeber that")
        if character[1] in mine:
            raise ValueError("Oops you can't eat your peaces")
        nx= from_row + dx
        ny = from_col + dy
        for i in lst:
            x, y = i
            d_x = nx + x
            d_y = ny + y
            if d_x >= 8 or d_y >= 8 or d_x < 0 or d_y < 0:
                continue
            char = grid[d_y][d_x].value
            char = char.split(":")
            if char[1] == "k":
                raise ValueError("Oops you can't be near like that with the king your not the queen")       
        if character[1] in mine:
            raise ValueError("Oops you can't eat your peaces")
        if oppon[1] in opponent:
            grid[from_col][from_row].value = charac[0]+":"+"#"
            boerd[from_col][from_row] = grid[from_col][from_row].value
    
    except ValueError as e:
        print("Error:",e)
        return False
    return True




def rule_knight(from_n, to, boerd, grid):
    from_row, from_col = ft_position(from_n,boerd)
    to_row, to_col = ft_position(to,boerd)
    dx = from_row - to_row
    dy = from_col - to_col
    character = to.split(":")
    mine = ['R','N','B','Q','K','P']
    try:
        if sorted([abs(dx),abs(dy)]) != [1, 2]:
            raise ValueError("you are knight remeber that")
        if character[1] in mine:
            raise ValueError("Oops you can't eat your peaces")
    
    except ValueError as e:
        print("Error:",e)
        return False
    return True



def rule_check_bishop(from_p , to, boerd, grid):
    character = from_p.split(":")
    oppon = to.split(":")
    friendly = ['B','#']
    opponent = ['p','r','b','q','n']
    mine = ['R','N','B','Q','K','P']
    from_row, from_col = ft_position(from_p,boerd)
    to_row, to_col = ft_position(to,boerd)
    f_r = from_row
    f_c = from_col

    try:
        if abs(from_row - to_row) != abs(from_col - to_col):
            raise ValueError("please move the bishop so form like x")
        dy = (to_col > from_col) - (to_col < from_col)
        dx = (to_row > from_row) - (to_row < from_row)
        if dx == 0 or dy == 0:
            return False
        while True:
            from_row +=dx
            from_col +=dy
            value = boerd[from_row][from_col].split(":")
            if from_col == to_col or from_row == to_row:
                break
            if value[1] in mine:
                raise ValueError("friends")
                break
        if oppon[1] in opponent:
            grid[f_r][f_c].value = character[0]+":"+"#"
            boerd[f_r][f_c] = grid[f_r][f_c].value
    except ValueError as e:
        print("Error", e)  
        return False
    return True
    

def rule_rock(from_r, to, boerd, grid):
    check = ['R','N','B','Q','K','p','r','b','q','n']
    oppon = to.split(":")
    character = from_r.split(":")
    
    from_row, from_col = ft_position(from_r,boerd)
    to_row, to_col = ft_position(to,boerd)
    
    f_r = from_row
    f_c = from_col
    try:
        if abs(from_row - to_row) == abs(from_col - to_col):
            raise ValueError("you can't move diagonal")
        row_move = from_row - to_row
        col_move = from_col - to_col 
        dx = (from_row >= to_row) - (from_row <= to_row)
        dy = (from_col >= to_col) - (from_col <= to_col)
        while True:
            from_row +=dx
            from_col +=dy
            if from_col == to_col or from_row == to_row:
                break
            value = boerd[from_row][from_col].split(":")
            if value[1] in check:
                raise ValueError("R you can't jump hhhh u are not Knight")
                break
          
        if oppon[1] in opponent:
            grid[f_r][f_c].value = character[0]+":"+"#"
            boerd[f_r][f_c] = grid[f_r][f_c].value
    except ValueError as e:
        print("Error",e)
        return False
    return True


def rule_queen(from_q, to, boerd, grid):
    return rule_check_bishop(from_q, to, boerd, grid) or from_q, to, boerd, grid

def check_and_move(first, second,peace, boerd,grid,turn):
    fro_m = first
    to = second
    rule = {
        "P": rule_move_pawn_white,
        "B": rule_check_bishop,
        "R":rule_rock,
        "Q":rule_queen,
        "N":rule_knight,
        "K":rule_king,
        "E":rule_checks
    }
    check_move = rule.get(peace,lambda *args : False)(fro_m , to, boerd, grid)
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
        elif peace == "r":
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

