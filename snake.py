from curses import wrapper
import curses
import sys
import random 
from time import sleep
import time 
# the problem that i will solve it later is the mose is showing also the charater is move with mose
class Snake:
    def control_snake(self, stdscr):
        character = "🐉"
        # character = "🐀"
        food = "🍥"
        curses.curs_set(0)
        height, width = stdscr.getmaxyx()
        row = width // 2
        col = height // 2
        stdscr.addstr(col, row, character)
        food_hieght = random.randint(0, height -1)
        food_width = random.randint(0, width - 1)
        stdscr.addstr(food_hieght, food_width, food)
        stdscr.border()
        check_food = 0
        while True:
            
            height_new, width_new = stdscr.getmaxyx()
            if height != height_new or width != width_new:
                stdscr.clear()
                height = height_new
                width = width_new
                row = width // 2
                col = height // 2

                stdscr.addstr(col, row, character)
                food_hieght = random.randint(0, height -1)
                food_width = random.randint(0, width - 1)
                stdscr.addstr(food_hieght, food_width, food)
                # stdscr.addstr(5,5, f"height : {height} width : {width}")
                stdscr.refresh()

            stdscr.border()
            key = stdscr.getkey()
            if key == "KEY_UP" and col != 0:
                
                
                stdscr.erase()
                col -= 1
                stdscr.addstr(food_hieght, food_width, food)
                stdscr.addstr(col, row, character)
                if col == food_hieght and row == food_width:
                    check_food +=1
                    food_hieght = random.randint(0, height -1)
                    food_width = random.randint(0, width - 1)
                    stdscr.addstr(food_hieght, food_width, food)
                    time.sleep()
                    
                stdscr.refresh()
            if key == "KEY_DOWN" and col +1!= height:
                stdscr.erase()
                col = col + 1
                stdscr.addstr(food_hieght, food_width, food)
                stdscr.addstr(col, row, character)
                if col == food_hieght and row == food_width:
                    food_hieght = random.randint(0, height -1)
                    food_width = random.randint(0, width - 1)
                    stdscr.addstr(food_hieght, food_width, food)
                stdscr.refresh()
            if key == "KEY_RIGHT" and row + 1!= width -1:
                stdscr.erase()
                row = row + 1
                # stdscr.refresh()
                stdscr.addstr(food_hieght, food_width, food)
                stdscr.addstr(col, row, character)
                if col == food_hieght and row == food_width:
                    food_hieght = random.randint(0, height -1)
                    food_width = random.randint(0, width - 1)
                    stdscr.addstr(food_hieght, food_width, food)
                stdscr.refresh()
            if key == "KEY_LEFT" and row != 0:
                stdscr.erase()
                row -= 1
                stdscr.addstr(food_hieght, food_width, food)
                stdscr.addstr(col, row, character)
                if col == food_hieght and row == food_width:
                    food_hieght = random.randint(0, height -1)
                    food_width = random.randint(0, width - 1)
                    stdscr.addstr(food_hieght, food_width, food)
                stdscr.refresh()
            if key == "q" or col + 1 == height or col == 0 or row+1 == width - 1 or row == 0:
                sys.exit()
                stdscr.erase()
                stdscr.getch()
                stdscr.refresh()
            # else:
                # stdscr.addstr(col+1, row, character)
            # if key == curses.KEY_RESIZE:
            #     break
#replace clear with erase
#curs_set
snake = Snake()
curses.wrapper(snake.control_snake)

















    # def control_snake(self, stdscr):
    #     stdscr.clear()
    #     stdscr.addstr(0,0, "hello world")
    #     stdscr.refresh()
    #     key = stdscr.getkey()

    #     stdscr.addstr(5,5, key)

    #     stdscr.refresh()

    #     stdscr.getch()
    #origine hiegh 21 and the width 160
    #157, 10 , 160, 
    # width:158 ,height 10