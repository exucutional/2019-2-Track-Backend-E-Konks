#! /usr/bin/env python
from unittest.mock import patch
from io import StringIO
import unittest

class TicTacToe:
    def __init__(self):
        self.__grid = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]
        self.__end = False


    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, value):
        assert(isinstance(value, list))
        assert(len(value) == 9)
        self.__grid = value


    def draw_grid(self):
        print("Current grid:             Model:")
        for i in range(3):
            cell1 = self.__grid[i*3] if self.__grid[i*3] else " "
            cell2 = self.__grid[i*3 + 1] if self.__grid[i*3 + 1] else " "
            cell3 = self.__grid[i*3 + 2] if self.__grid[i*3 + 2] else " "

            cell1_t = i*3 if not self.__grid[i*3] else " "
            cell2_t = i*3 + 1 if not self.__grid[i*3 + 1] else " "
            cell3_t = i*3 + 2 if not self.__grid[i*3 + 2] else " "

            strf = f" {cell1} █ {cell2} █ {cell3}                 {cell1_t} █ {cell2_t} █ {cell3_t}"
            print(strf)
            if i < 2:
                print("■■■█■■■█■■■               ■■■█■■■█■■■")


    def check_win(self):
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
            res = res or self.check_pos(*option)

        return res


    def check_pos(self, pos0, pos1, pos2):
        mark = self.__grid[pos0]
        return mark != 0 and mark == self.__grid[pos1] and mark == self.__grid[pos2]


    def check_draw(self):
        res = True
        for cell in self.__grid:
            res = res and cell

        return bool(res)


    def play(self):
        player1_mark = ''
        draw = False
        while player1_mark != 'X' and player1_mark != 'O':
            player1_mark = input("Choose player1's mark['X' or 'O']: ")
            if player1_mark != 'X' and player1_mark != 'O':
                print("___________ERROR: Wrong mark")


        mark = player1_mark
        while not self.__end:
            self.draw_grid()
            #self.draw_input_grid()
            if mark == player1_mark:
                cell = input(f"Player1 '{mark}' choose your cell: ")
            else:
                cell = input(f"Player2 '{mark} choose your cell: ")

            try:
                cell = int(cell)
            except ValueError:
                print(f"__________ERROR: Wrong input: {cell}")
                continue

            if not (0 <= cell < 9) or self.__grid[cell] != 0:
                print(f"__________ERROR: Wrong number: {cell}")
                continue

            print("__________________________________________________")
            self.__grid[cell] = mark
            if self.check_win():
                self.__end = True
            elif self.check_draw():
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



class TestTicTacToe(unittest.TestCase):
    def test_draw_win(self):
        game = TicTacToe()
        game.grid = [
            'X', 'X', 'O',
            'O', 'X', 'X',
            'X', 'O', 'O'
        ]
        self.assertEqual(game.check_draw(), True)
        self.assertEqual(game.check_win(), False)
        game.grid = [
            'X', 'X', 'X',
            0, 0, 0,
            0, 0, 0
        ]
        self.assertEqual(game.check_draw(), False)
        self.assertEqual(game.check_win(), True)


    def test_pos(self):
        game = TicTacToe()
        game.grid = [
            'X', 'O', 'X',
            'O', 'X', 'O',
            'X', 'O', 'X'
        ]
        self.assertEqual(game.check_pos(0, 1, 2), False)
        self.assertEqual(game.check_pos(0, 3, 6), False)
        self.assertEqual(game.check_pos(0, 4, 8), True)


    def test_play(self):
        inp = ['X', 0, 1, 2, 3, 4, 5, 6, 7]
        with patch('builtins.input', side_effect=inp), patch('sys.stdout', new=StringIO()) as fake:
            game = TicTacToe()
            game.play()



if __name__ == "__main__":
    #unittest.main()
    Game = TicTacToe()
    Game.play()
