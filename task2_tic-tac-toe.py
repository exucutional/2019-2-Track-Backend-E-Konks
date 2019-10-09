#! /usr/bin/env python
class TicTacToe:
    def __init__(self):
        self.__grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__end = False 


    def draw_grid(self):
        print("Current grid:             Model:")
        for i in range(3):
            cell1 = self.__grid[i*3] if self.__grid[i*3] else " "
            cell2 = self.__grid[i*3 + 1] if self.__grid[i*3 + 1] else " "
            cell3 = self.__grid[i*3 + 2] if self.__grid[i*3 + 2] else " "

            cell1_t = i*3 if not self.__grid[i*3] else " "
            cell2_t = i*3 + 1 if not self.__grid[i*3 + 1] else " "
            cell3_t = i*3 + 2 if not self.__grid[i*3 + 2] else " "

            str = f" {cell1} █ {cell2} █ {cell3}                 {cell1_t} █ {cell2_t} █ {cell3_t}"
            print(str)
            if i < 2:
                print("■■■█■■■█■■■               ■■■█■■■█■■■")


    def __check_win(self):
        res = False
        options = [
            (0, 1, 2),
            (0, 3, 6),
            (0, 4, 8),
            (6, 7, 8),
            (6, 4, 2),
            (2, 5, 8)
        ]
        for option in options:
            res = res or self.__check_pos(*option)

        return res


    def __check_pos(self, pos0, pos1, pos2):
        mark = self.__grid[pos0]
        return mark != 0 and mark == self.__grid[pos1] and mark == self.__grid[pos2] 


    def __check_draw(self):
        res = True
        for cell in self.__grid:
            res = res and cell

        return res


    def play(self):
        player1_mark = ''
        draw = False
        while player1_mark != 'X' and player1_mark != 'O':
            player1_mark = input("Choose player1's mark['X' or 'O']: ")
            if player1_mark != 'X' and player1_mark != 'O':
                print("___________ERROR: Wrong mark")


        mark = player1_mark
        while (not self.__end):
            self.draw_grid()
            #self.draw_input_grid()
            if mark == player1_mark:
                cell = input("Player1 choose your cell: ")
            else:
                cell = input("Player2 choose your cell: ")

            try:
                cell = int(cell)
            except ValueError:
                print("__________ERROR: Wrong input")
                continue
            
            if not (0 <= cell < 9) or self.__grid[cell] != 0:
                print("__________ERROR: Wrong number")
                continue
            
            print("__________________________________________________")
            self.__grid[cell] = mark
            if self.__check_win():
                self.__end = True
            elif self.__check_draw():
                self.__end = True
                draw = True
            else:
                mark = 'X' if mark == 'O' else 'O'
        if draw:
            print("_____DRAW!_____")
        elif mark == player1_mark:
            print(f"_____PLAYER1 '{mark}' WINS!_____")
        else:
            print(f"_____PLAYER2 '{mark}' WINS!_____")
        
        self.draw_grid()



if __name__ == "__main__":
    game = TicTacToe()
    game.play()
