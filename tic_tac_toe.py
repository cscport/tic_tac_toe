import re
from random import randint

class TicTacToe:

    def __init__(self):
        self.game_over = False
        self.board = []
        for i in range(3):
            row = []
            for ri in range(3):
                row.append("-")
            self.board.append(row)

    def get_user_symbol(self):
        valid_X = re.compile("^\s*[X|x]\s*$")
        valid_O = re.compile("^\s*[O|o]\s*$")
        user_input = raw_input("Would you like to be X or O?: ")
        if user_input and valid_X.match(user_input):
            self.user_symbol = "X"
            self.computer_symbol = "O"
        elif user_input and valid_O.match(user_input):
            self.user_symbol = "O"
            self.computer_symbol = "X"
        else:
            print "Please choose a correct symbol"
            self.get_user_symbol()

    def print_board(self):
        for row in self.board:
            print row

        print "========================================"

    def get_move(self, symbol):
        if self.user_symbol == symbol:
            self.get_user_move()
        else:
            self.get_computer_move()

    def get_user_move(self):
        valid_input = re.compile("^\s*[0|1|2]\s[0|1|2]\s*$")
        user_input = raw_input("Please make a move (x, y): ")
        if user_input and valid_input.match(user_input):
            user_input = user_input.strip().split(" ")
            x = int(user_input[0])
            y = int(user_input[1])
        else:
            print "Please enter your move in a valid location or format!"
            self.get_user_move()

        if self.board[x][y] == "-":
            self.board[x][y] = self.user_symbol
        else:
            print "That square is already taken!"
            self.get_user_move()

    def get_computer_move(self):
        x = randint(0, 2)
        y = randint(0, 2)
        if self.board[x][y] == "-":
            self.board[x][y] = self.computer_symbol
        else:
            self.get_computer_move()


    def check_game_over(self):
        board = self.board

        for row in board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != "-":
                self.winner = row[0]
                self.game_over = True

        # vertical
        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
                self.winner = board[0][i]
                self.game_over = True

        # criss cross
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-":
            self.winner = board[0][0]
            self.game_over = True

        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "-":
            self.winner = board[0][2]
            self.game_over = True

    def print_concluding_message(self):
        self.print_board()
        print "%s is the winner!" % self.winner

    def user_wants_to_play_again(self):
        user_input = raw_input("Would you like to play again?: [Y/n] ")
        return not user_input or user_input[0].lower == "y"

    def start_game(self):
        print "Let's play tic tac toe!"
        self.get_user_symbol()
        self.print_board()
        while not self.game_over:
            self.get_move("X")
            self.print_board()
            self.check_game_over()
            if not self.game_over:
                self.get_move("O")
                self.print_board()
                self.check_game_over()
        self.print_concluding_message()
        if self.user_wants_to_play_again():
            self.__init__()
            self.start_game()
        else:
            print "Thanks for playing! Good bye."


tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()

