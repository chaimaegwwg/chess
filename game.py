from typing import List
import sys
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
                boerd_arr.append(f"{i}{x}:p")
            elif x == 2:
                boerd_arr.append(f"{i}{x}:P")
            elif f"{i}{x}" == "a8" or f"{i}{x}" == "h8":
                boerd_arr.append(f"{i}{x}:r")
            elif f"{i}{x}" == "b8" or f"{i}{x}" == "g8":
                boerd_arr.append(f"{i}{x}:n")
            elif f"{i}{x}" == "c8" or f"{i}{x}" == "f8":
                boerd_arr.append(f"{i}{x}:b")
            elif f"{i}{x}" == "d8":
                boerd_arr.append(f"{i}{x}:q")
            elif f"{i}{x}" == "e8":
                boerd_arr.append(f"{i}{x}:k")
            elif f"{i}{x}" == "a1" or f"{i}{x}" == "h1":
                boerd_arr.append(f"{i}{x}:R")
            elif f"{i}{x}" == "b1" or f"{i}{x}" == "g1":
                boerd_arr.append(f"{i}{x}:N")
            elif f"{i}{x}" == "c1" or f"{i}{x}" == "f1":
                boerd_arr.append(f"{i}{x}:B")
            elif f"{i}{x}" == "d1":
                boerd_arr.append(f"{i}{x}:Q")
            elif f"{i}{x}" == "e1":
                boerd_arr.append(f"{i}{x}:K")  
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
                print(f"|\033[90m{e}\033[97m|", end = " ")
            else:    
                print(f"|\033[97m{e}\033[97m|", end = " ")
        print()
    for _ in range(8):
            print("----- ", end = " ")
    print()
#this function is move on generale peaces and replace it 
# def get_info():
#     boerd = ft_boerd()
#     render(boerd)
#     try:
#         first = str(input("Please entery the peace that u want to move it from: "))
#         second = str(input("Please entery the peace that u want to move it to : "))
#     except:
#         sys.exit()
#     if not any(first in row for row in boerd):
#         print("Please enter a number of square")
#         sys.exit()
#     return (first,second,boerd)
 









# pieces = {
#     'white': {'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'},
#     'black': {'K': '♚', 'Q': '♛', 'R': '♜', 'B': '♝', 'N': '♞', 'P': '♟'}
# }
# boerd = ft_boerd()
# print(boerd)