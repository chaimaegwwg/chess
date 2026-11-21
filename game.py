from typing import List
import pygame
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
#this i will change on it 
# def render(boerd):
#     usage = []
#     for i in boerd:
#         for _ in range(8):
#             print("----- ", end = " ")
#         print()
#         for e in i:
#             if "#" in e:
#                 print(f"|\033[90m{e}\033[97m|", end = " ")
#             else:    
#                 print(f"|\033[97m{e}\033[97m|", end = " ")
#         print()
#     for _ in range(8):
#             print("----- ", end = " ")
#     print()

def render(boerd):
    pygame.init()
    line_color = (40, 28, 15)
    screen = pygame.display.set_mode((900, 900))

    black = (0, 0, 0)
    white = (255, 255, 255)
    size_cell = 900//8
    check = 1
    usage = []
    font = pygame.font.SysFont(None, 50)
    for row in range(8):
        # for i in range(8):
        #     pygame.draw.line(screen,line_color,(i),(i),5)
        # # print()
        for col in range(8):
            # print("herrrrrrrrrrrrrrrrre",e)
            if check == 1:
                check = -1
                color = white
            else:
                check = 1
                color = black
            x = col *size_cell
            y = row *size_cell

            pygame.draw.rect(screen, color ,(x,y,size_cell,size_cell))
            
            text_surface = font.render(boerd[row][col], True, (255, 165, 0))

            screen.blit(text_surface, ((col*size_cell)+15, (row*size_cell)+40))
       
            pygame.display.flip()
        if check == 1:
            check = -1
        else:
            check = 1 
        
            # if "#" in e:
            #     print(f"|\033[90m{e}\033[97m|", end = " ")
            # else:    
            #     print(f"|\033[97m{e}\033[97m|", end = " ")
        # print()
    # for n in range(8):
    #         # print("----- ", end = " ")
    #         pygame.draw.line(screen,line_color,(n),(n),5)
    # print()


# def display():
#     pygame.init()
#     black = (0,0,0)
#     font = pygame.font.Font(None, 40)
#     cell_size = 50
#     usage = []
#     for i in boerd:
#         for _ in range(8):
#             print("----- ", end = " ")
#         print()
#         for e in i:
#             if "#" in e:
#                 print(f"|\033[90m{e}\033[97m|", end = " ")
#             else:    
#                 print(f"|\033[97m{e}\033[97m|", end = " ")
#         print()
#     for _ in range(8):
#             print("----- ", end = " ")
#     print()
     

# display()
# def display(self,pos,food,super_pacgums):
#     pygame.init()
#     black = (0, 0, 0)
#     font = pygame.font.Font(None, 40)
#     cell_size = self.size_cell
#     for row, line in enumerate(self.generator.maze):
#         for col, cell in enumerate(line):
#             x = col * cell_size
#             y = row * cell_size
          
#             if cell & 1:
#                 pygame.draw.line(self.screen, (100, 80, 120),(x, y),(x + cell_size, y), 3)
    
#             if cell & 2:
#                 pygame.draw.line(self.screen, (100, 80, 120),(x + cell_size, y),(x + cell_size, y + cell_size), 3)
        
#             if cell & 4:
#                 pygame.draw.line(self.screen, (100, 80, 120),(x, y + cell_size),(x + cell_size, y + cell_size), 3)
#             if cell & 8:
#                 pygame.draw.line(self.screen, (100, 80, 120),(x, y),(x, y + cell_size), 3)
#     return food,super_pacgums

