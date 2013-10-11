#!/usr/bin/python
from __future__ import unicode_literals
import re
#from collections import namedtuple


class Piece(object):
    def __init__(self, color):
        self._algebraic = None
        self.color = color

    def __repr__(self):
        return self.__class__.__name__.lower()

    def algebraic(self):
        return self._algebraic


class Pawn(Piece):
    def __init__(self, color):
        self._algebraic = '(P)'
        self.color = color


class Rook(Piece):
    def __init__(self, color):
        self._algebraic = 'R'
        self.color = color


class Knight(Piece):
    def __init__(self, color):
        self._algebraic = 'N'
        self.color = color


class Bishop(Piece):
    def __init__(self, color):
        self._algebraic = 'B'
        self.color = color


class Queen(Rook, Bishop):
    def __init__(self, color):
        self._algebraic = 'Q'
        self.color = color


class King(Piece):
    def __init__(self, color):
        self._algebraic = 'K'
        self.color = color


class Square(object):
    def __init__(self, x, y, current_piece=None):
        self.x = x
        self.y = y
        self.current_piece = current_piece

    def __repr__(self):
        return self.get_algebraic()

    def get_algebraic(self):
        if self.current_piece:
            return '%s%s%s' % (self.current_piece.algebraic(),
                               self.x, self.y)
        else:
            return '%s%s' % (self.x, self.y)


class Board(object):
    def __init__(self):
        x_axis = [chr(i) for i in xrange(97, 105)]
        y_axis = [i for i in xrange(1, 9)]
        self.squares = [Square(x, y)
                        for x in x_axis
                        for y in y_axis]
        self._white_back_row_order = [Rook,
                                      Knight,
                                      Bishop,
                                      Queen,
                                      King,
                                      Bishop,
                                      Knight,
                                      Rook,
                                      ]
        self.reset_game()

    def reset_game(self):
        self._reset_pawns()
        self._reset_white_back_row()
        self._reset_black_back_row()

    def _reset_pawns(self):
        for row, color in [(2, 'white'), (7, 'black')]:
            for square in self.get_row(row):
                square.current_piece = Pawn(color)

    def _reset_white_back_row(self):
        back_row_pieces = self._white_back_row_order
        for column, square in enumerate(self.get_row(1)):
            square.current_piece = back_row_pieces[column]('white')

    def _reset_black_back_row(self):
        back_row_pieces = self._white_back_row_order
        # Fix black's ordering, switch queen and king
        back_row_pieces[3:5] = [King, Queen]
        for column, square in enumerate(self.get_row(1)):
            square.current_piece = back_row_pieces[column]('black')

    def get_row(self, row_num):
        """
        Returns a list of squares from a particular row on the x-axis.
        """
        return [square
                for square in self.squares
                if square.y == row_num]

    def get_all_rows(self, reverse=True):
        if reverse:
            return [self.get_row(i)
                    for i in xrange(8, 0, -1)]
        else:
            return [self.get_row(i)
                    for i in xrange(1, 9)]


class Game(object):
    def __init__(self):
        self.board = Board()

    def print_layout(self):
        for row in self.board.get_all_rows():
            print ' | '.join([square.get_algebraic()
                              for square in row])

    def parse_move(self, move_input):
        pass



if __name__ == '__main__':
    game = Game()
    game.print_layout()
    while True:
        move = raw_input("Your move> ")
        game.parse_move(move)