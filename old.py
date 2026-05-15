from typing import List
import sys
#old that i love the visilusation
#mission is to move the peaces from to go 
#the problem that it regenerate
#mission is to controle the pawn 
def ft_boerd() -> List[List[str]]:
    lst = ["a", "b", "c", "d", "e", "f", "g", "h"]

    boerd = []
    boerd_arr = []
    for x in range(8,0,-1):
        boerd_arr = []
        for i in lst:
            if x == 7:
                boerd_arr.append(f"{i}{x}:♙")
            elif x == 2:
                boerd_arr.append(f"{i}{x}:♟")
            elif f"{i}{x}" == "a8" or f"{i}{x}" == "h8":
                boerd_arr.append(f"{i}{x}:♖")
            elif f"{i}{x}" == "b8" or f"{i}{x}" == "g8":
                boerd_arr.append(f"{i}{x}:♘")
            elif f"{i}{x}" == "c8" or f"{i}{x}" == "f8":
                boerd_arr.append(f"{i}{x}:♗")
            elif f"{i}{x}" == "d8":
                boerd_arr.append(f"{i}{x}:♕")
            elif f"{i}{x}" == "e8":
                boerd_arr.append(f"{i}{x}:♔")
            elif f"{i}{x}" == "a1" or f"{i}{x}" == "h1":
                boerd_arr.append(f"{i}{x}:♖")
            elif f"{i}{x}" == "b1" or f"{i}{x}" == "g1":
                boerd_arr.append(f"{i}{x}:♘")
            elif f"{i}{x}" == "c1" or f"{i}{x}" == "f1":
                boerd_arr.append(f"{i}{x}:♗")
            elif f"{i}{x}" == "d1":
                boerd_arr.append(f"{i}{x}:♕")
            elif f"{i}{x}" == "e1":
                boerd_arr.append(f"{i}{x}:♔")  
            else:
                boerd_arr.append(f"{i}{x}:#")
        boerd.append(boerd_arr)
    return boerd

def render(boerd):
    usage = []
    for i in boerd:
        for _ in range(8):
            print("----- ", end = " ")
        print()
        for e in i:
            if "#" in e:
                print(f"|\033[90m{e}\033[0m|", end = " ")
            else:    
                print(f"|{e}|", end = " ")
        print()
    for _ in range(8):
            print("----- ", end = " ")
    print()
#this function is move on generale peaces and replace it 
def move_generale_from_to():
    boerd = ft_boerd()
    render(boerd)
    try:
        first = str(input("Please entery the peace that u want to move it from: "))
        second = str(input("Please entery the peace that u want to move it to : "))
    except:
        sys.exit()
    if not any(first in row for row in boerd):
        print("Please enter a number of square")
        sys.exit()
    fro_m = first.split(":")
    to = second.split(":")
    temp = fro_m[1]
    for row in range(8):
        for i in range(8):
            if boerd[row][i] == first:
                boerd[row][i] = str(fro_m[0]+":"+to[1])
            elif boerd[row][i] == second:
                boerd[row][i] = str(to[0]+":"+temp)

    render(boerd)

def controle_pawn():
    pass
move_generale_from_to()










# pieces = {
#     'white': {'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'},
#     'black': {'K': '♚', 'Q': '♛', 'R': '♜', 'B': '♝', 'N': '♞', 'P': '♟'}
# }
# boerd = ft_boerd()
# print(boerd)