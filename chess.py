
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšáka.
        
        Uvažujeme pouze pohyb vpřed bez braní a bez dvojkroku.
        - Bílý pěšák: row se zvyšuje o 1.
        - Černý pěšák: row se snižuje o 1.
        """
        row, col = self.position
        
        if self.color == "white":
            new_position = (row + 1, col)
        else:  # "black"
            new_position = (row - 1, col)

        if self.is_position_on_board(new_position):
            return [new_position]
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        Střelec se pohybuje po diagonálách libovolný počet polí.
        """
        row, col = self.position
        final_moves = []

        # Všechny čtyři diagonální směry (delta_row, delta_col)
        directions = [
            (1, 1),   # dolů vpravo
            (1, -1),  # dolů vlevo
            (-1, 1),  # nahoru vpravo
            (-1, -1)  # nahoru vlevo
        ]

        for d_row, d_col in directions:
            current_row = row + d_row
            current_col = col + d_col
            while self.is_position_on_board((current_row, current_col)):
                final_moves.append((current_row, current_col))
                current_row += d_row
                current_col += d_col

        return final_moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        Věž se pohybuje vodorovně a svisle libovolný počet polí.
        """
        row, col = self.position
        final_moves = []

        # Směry: nahoru, dolů, doprava, doleva
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1)   # doleva
        ]

        for d_row, d_col in directions:
            current_row = row + d_row
            current_col = col + d_col
            while self.is_position_on_board((current_row, current_col)):
                final_moves.append((current_row, current_col))
                current_row += d_row
                current_col += d_col

        return final_moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.
        Dáma kombinuje pohyb věže a střelce: 8 směrů libovolný počet polí.
        """
        row, col = self.position
        final_moves = []

        # 8 směrů: 4 rovné (věž) + 4 diagonály (střelec)
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1),  # doleva
            (1, 1),   # dolů vpravo
            (1, -1),  # dolů vlevo
            (-1, 1),  # nahoru vpravo
            (-1, -1)  # nahoru vlevo
        ]

        for d_row, d_col in directions:
            current_row = row + d_row
            current_col = col + d_col
            while self.is_position_on_board((current_row, current_col)):
                final_moves.append((current_row, current_col))
                current_row += d_row
                current_col += d_col

        return final_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        Král se pohybuje o jedno pole do libovolného z 8 směrů.
        """
        row, col = self.position
        moves = [
            (row + 1, col),     # dolů
            (row - 1, col),     # nahoru
            (row, col + 1),     # doprava
            (row, col - 1),     # doleva
            (row + 1, col + 1), # dolů vpravo
            (row + 1, col - 1), # dolů vlevo
            (row - 1, col + 1), # nahoru vpravo
            (row - 1, col - 1)  # nahoru vlevo
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Knight("black", (1, 2)),
        Pawn("white", (2, 2)),
        Pawn("black", (7, 2)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("white", (4, 4)),
        King("black", (8, 5)),
    ]

    for piece in pieces:
        print(piece)
        print(piece.possible_moves())
        print("---")
