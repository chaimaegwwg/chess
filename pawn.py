from game import render,ft_boerd
import sys
import pygame


class Step:
    def __init__(self, col, row,value,move_king):
        self.visited = 0
        self.col = col
        self.row = row
        self.value = value
        self.move_king = move_king


def inside_class():
    boerd = ft_boerd()
    steps_grid = []
    for x in range(8):
        row_list = []
        for y in range(8):
            step = Step(x,y,boerd[x][y],0)
            row_list.append(step)
        steps_grid.append(row_list)
    return steps_grid

def ft_position_character(from_p, boerd):
    for row in range(8):
        for col in range(8):
            ch = boerd[row][col].split(":")
            if ch[1] == from_p:
                return (row, col)
    return (0,0)

def ft_position(from_p, boerd):
    for row in range(8):
        for col in range(8):
            if boerd[row][col] == from_p:
                return (row, col)
    return (0,0)


def rule_move_pawn_white(from_p, to , boerd,grid,turn):
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

def rule_move_pawn_black(from_p, to, boerd, grid,turn):
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
    #here it already changed
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



def rule_king(from_k, to, boerd, grid,turn):
    from_col ,from_row = ft_position(from_k,boerd)
    to_col ,to_row = ft_position(to,boerd)
    char = grid[from_col][from_row].value
    char = char.split(":")
    charac = from_k.split(":")
    dx = to_row - from_row
    dy = to_col - from_col
    if turn == 1: 
        opponent = ['p','r','b','q','n']
        mine = ['R','N','B','Q','P',"K"]
    else:
        opponent = ['R','N','B','Q','P']
        mine = ['p','r','b','q','n',"k"]
    
    oppon = to.split(":")
    character = to.split(":")
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
            # if char[1] == "k":
            #     raise ValueError("Oops you can't be near like that with the king your not the queen")       
        if character[1] in mine:
            raise ValueError("Oops you can't eat your peaces")
        if oppon[1] in opponent:
            grid[from_col][from_row].value = charac[0]+":"+"#"
            boerd[from_col][from_row] = grid[from_col][from_row].value
    
    except ValueError as e:
        print("Error:",e)
        return False
    return True




def rule_knight(from_n, to, boerd, grid,turn):
    from_row, from_col = ft_position(from_n,boerd)
    to_row, to_col = ft_position(to,boerd)
    dx = from_row - to_row
    dy = from_col - to_col
    character = to.split(":")
    charac = from_n.split(":")
    mine = []
    print("whaaaaaaaaaaat is the problem", character,character[1])
    if turn == 1:
        mine = ['R','N','B','Q','K','P']
        opponent = ['r','n','b','q','k','p']
    else:
        opponent = ['R','N','B','Q','K','P']
        mine = ['r','n','b','q','k','p']
    try:
        if sorted([abs(dx),abs(dy)]) != [1, 2]:
            raise ValueError("you are knight remeber that")
        if character[1] in mine:
            raise ValueError("Oops you can't eat your peaces")
        if character[1] in opponent:
            grid[from_col][from_row].value = charac[0]+":"+"#"
            boerd[from_col][from_row] = grid[from_col][from_row].value

    
    except ValueError as e:
        print("Error:",e)
        return False
    return True



def rule_check_bishop(from_p , to, boerd, grid,turn):
    character = from_p.split(":")
    oppon = to.split(":")
    if turn == 1:
        friendly = ['B','#']
        opponent = ['p','r','b','q','n']
        mine = ['R','N','B','Q','K','P']
    else:
        friendly = ['b','#']
        opponent = ['P','R','B','Q','N']
        mine = ['r','n','b','q','k','p']
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
    

def rule_rock(fro_m, to, boerd, grid,turn):
    oppon = to.split(":")
    character = fro_m.split(":")
    check = ['R','N','B','Q','K','p','r','b','q','n']
    if turn == 1:
        opponent = ['B','K','B','Q','R']
    else:
        opponent = ['b','k','b','q','r']
        print("he se the oppent")
    from_row, from_col = ft_position(fro_m,boerd)
    to_row, to_col = ft_position(to,boerd)
    
    f_r = from_row
    f_c = from_col
    try:
        if abs(from_row - to_row) == abs(from_col - to_col):
            raise ValueError("you can't move diagonal")
        row_move = from_row - to_row
        col_move = from_col - to_col 
        dx = (from_row <= to_row) - (from_row >= to_row)
        dy = (from_col <= to_col) - (from_col >= to_col)
        # print("this print is for dx and dy",dx,dy, from_row,from_col,to_row,to_col)
        while True:
            from_row +=dx
            from_col +=dy
            if from_col == to_col and from_row == to_row:
                # print("it do it hereee",from_row,from_col,to_row,to_col)
                break
            # print("this is for check the from_row and col_row and to col and to row", from_row,from_col,to_row,to_col)
            value = boerd[from_row][from_col].split(":")
            # print("this the value for check ",value)
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




def rule_queen(from_q, to, boerd, grid,turn):
    return rule_check_bishop(from_q, to, boerd, grid,turn) or rule_rock(from_q, to, boerd, grid,turn)

# here for the while is true may it will be error on the future because it didin't check the limit of the boerd


def check_king_rock(from_row, from_col, dx, dy, boerd):
    row = from_row + dx
    col = from_col + dy
    Flag = False
    piece = False
    friends = ['R','N','B','Q','P','p','b','n']

    while True:

        if row <= 0 or row == 8 or col <= 0 or col == 8:
            print("the finale here")
            return [True,True,False]
        value = boerd[row][col].split(":")
        P = boerd[row][col]
        row += dx
        col += dy
        
        if value[1] == "#":
            print("it found like #",value[1])
            continue
        

        if value[1] == "r" or value[1] == "q" or value[1] == "b":
            if Flag is True and value[1] not in friends and value[1] != "#":
                print("this the value that is stop me", value[1])
                return [False,True,piece]
            else:
                return [True,False,piece]

        if value[1] in friends:
            print("this the value that is stop me -> ",value[1])
            Flag = True
            piece = P

    print("it finished but why")
   
    return [True,True,piece]

def check_king_rock_second_check(king_row, king_col,dx,dy,boerd):
    pass



def check_king_first(boerd, grid,piece):
    # pined peace is like the peace he see the rock p and u want to go this p should not go 
    king_row, king_col = ft_position_character("K",boerd)
    directions = [
        (-1,0), # up
        (1,0),  # down
        (0,-1), # left
        (0,1)   # right
    ]
    for dx,dy in directions:
        res = check_king_rock(king_row, king_col,dx,dy,boerd)
        # res_b = check_king_bishop(king_row, king_col,dx,dy,boerd)
        if not res[1]:
            print("it not check correct for the first")
            return False
        elif not res[0]:
            if res[2] == piece:
                print("the pined peace here u can't go this peace")
                print("=> if it is the origine bug",piece,res[2])
                return False
        #here should i add the Q ... not just the rock
    print("it check correctly for the first thing ")
    return True

#this is i hardcode it 
def ft_castl_king(first, second,fro_m, to, boerd):
    #first check if it left or right 
    #if any peace is between theme
    #if there is a a check on the king if that good do a move 



    king_row, king_col = ft_position_character("K",boerd)
    if first == "e1:K" and second == "h1:R":
        try:
            value1 = boerd[king_row][king_col+1].split(":")
            value2 = boerd[king_row][king_col+2].split(":")
        except:
            return boerd, False
        if value1[1] != "#" or value2[1] != "#":
            return boerd, False
        boerd = move_generale(first, "g1:#",fro_m, "g1:#", boerd)
        boerd = move_generale(second, "f1:#",second, "f1:#", boerd)
    elif first == "a1:R" and second == "e1:K":
        try:
            value1 = boerd[king_row][king_col-1].split(":")
            value2 = boerd[king_row][king_col-2].split(":")
            value3 = boerd[king_row][king_col-3].split(":")
        except:
            return boerd, False
        if value1[1] != "#" or value2[1] != "#" or value2[2] != "#":
            return boerd, False
        boerd = move_generale(first, "c1:#",fro_m, "c1:#", boerd)
        boerd = move_generale(second, "d1:#",second, "d1:#", boerd)
        


    return boerd, True


def check_and_move(first, second,peace, boerd,grid,turn):
    fro_m = first
    to = second
    #what meanning of E should i remove it!
    rule = {
        "P": rule_move_pawn_white,
        "B": rule_check_bishop,
        "R":rule_rock,
        "Q":rule_queen,
        "N":rule_knight,
        "K":rule_king,
        "E":rule_checks,
        # "r":rule_rock
    }
    print("check what is the peace ",grid[0][0].move_king)

    if peace == "K" and grid[0][0].move_king == 0:
        print("if it go on the right track")
        boerd,booling = ft_castl_king(first, second,fro_m, to, boerd)
        if booling is True:
            render(boerd)
            return True
    check_move = rule.get(peace,lambda *args : False)(fro_m , to, boerd, grid,1)
    if turn == "white":
        if check_move:
            if peace == "k":
                grid[0][0].move_king += 1
            boerd = move_generale(first, second,fro_m, to, boerd)
            render(boerd)
            return True
        else:
            return False
    else:
        rules = {
            "p": rule_move_pawn_black,
            "b": rule_check_bishop,
            "r":rule_rock,
            "q":rule_queen,
            "n":rule_knight,
            "k":rule_king,
            "e":rule_checks,
            # "r":rule_rock
        }
        check_move = rules.get(peace,lambda *args : False)(fro_m , to, boerd, grid,-1)

        # if peace == "p":
        #     check_move = rule_move_pawn_black(fro_m, to, boerd, grid)
        # elif peace == "B" or peace == "b":
        #     check_move = rule_check_bishop(fro_m , to, boerd, grid)
        # elif peace == "r":
        #     check_move = rule_rock(fro_m, to, boerd, grid)
        # elif peace == "n":
        #     check_move = rule_knight(fro_m, to, boerd, grid)
        # elif peace == "q":
        #     check_move = rule_queen(fro_m, to, boerd, grid)

        if check_move:
            boerd = move_generale(first, second,fro_m, to, boerd)
            render(boerd)
            return True
        else:
            return False

#i do it for don't change the real for that board
def ullition_boerd(first, second,peace, boerd,grid,turn):
    fro_m = first
    to = second
    rule = {
        "P": rule_move_pawn_white,
        "B": rule_check_bishop,
        "R":rule_rock,
        "Q":rule_queen,
        "N":rule_knight,
        "K":rule_king,
        "E":rule_checks,
        "r":rule_rock_black
    }
    
    check_move = rule.get(peace,lambda *args : False)(fro_m , to, boerd, grid)
    
    if turn == "white":
        if check_move:
            boerd = move_generale(first, second,fro_m, to, boerd)
            return True
        else:
            return False
    else:
        if peace == "p":
            check_move = rule_move_pawn_black(fro_m, to, boerd, grid)
        elif peace == "B" or peace == "b":
            check_move = check_bishop(fro_m , to, boerd, grid)
        elif peace == "r":
            check_move = rule_rock_black(fro_m, to, boerd, grid)

        if check_move:
            boerd = move_generale(first, second,fro_m, to, boerd)
            return True
        else:
            return False

def ft_predict_value_is_in(first,second, x_fr,boerd,grid,trun):
    king_row, king_col = ft_position_character("K",boerd)
    illution_boerd = [row.copy() for row in boerd]
    illution_grid = [row.copy() for row in grid]
    if not ullition_boerd(first, second, x_fr,illution_boerd,illution_grid,trun):
        return False
    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    

    for dx,dy in directions:
        if not check_king_first(illution_boerd,illution_grid,second):
            print("it not check correct for the first")
            return False
    
    print("it check correctly for the first thing ")
    return True

def check_peace_that_leave(first, second, x_fr, boerd,grid,trun):
    pass

def move_generale_from_to():
    grid = inside_class()
    boerd = ft_boerd()
    render(boerd)
    check = 1
    grid[0][0].move_king = 0
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
                check_king = check_king_first(boerd,grid,first)
                print("the first check the check king",check_king)
                if not check_king:
                    print("it do it first",check_king)
                    if not ft_predict_value_is_in(first, second, x_fr[1],boerd,grid,trun):
                        print("++++++++++++++++++++++it do continuee+++++++++++++++++")
                        print("hemida l moghamire defend u king or run")
                        continue
                else:
                    check_illution = check_peace_that_leave(first, second, x_fr[1],boerd,grid,trun)
                print("it gooooo")


                # if check_pined_peace(first, second, x_fr[1],boerd,grid,trun):
                #     pass
                
                
                if not check_and_move(first, second,x_fr[1],boerd,grid,trun):
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

