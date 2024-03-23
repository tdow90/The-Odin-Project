class TicTacToe:
    board = ["1","2","3","4","5","6","7","8","9"]

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name

    def print_board(self):
        print("\nCurrent positions: \n")
        for i in range(len(TicTacToe.board)):
            if (i+1)%3==0:
                print(TicTacToe.board[i], end="\n")
            else:
                print(TicTacToe.board[i], end=" ")

    def make_move(self):
        p1_move = int(input(f"{self.p1_name}, make a play: choose 1-9 to play that spot as X \n"))
        while TicTacToe.board[p1_move-1] == "X" or TicTacToe.board[p1_move-1] == "O":
            p1_move = int(input(f"{self.p1_name}, make another play, that position was already played:"))
        TicTacToe.board[p1_move-1] = "X"
        p2_move = int(input(f"{self.p2_name}, make a play: choose 1-9 to play that spot as O \n"))
        while TicTacToe.board[p2_move-1] == "X" or TicTacToe.board[p2_move-1] == "O":
            p2_move = int(input(f"{self.p2_name}, make another play, that position was already played:"))
        TicTacToe.board[p2_move-1] = "O"

    def check_winner(self):
        if TicTacToe.board[0]=="X" and TicTacToe.board[1]=="X" and TicTacToe.board[2]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[3]== "X" and TicTacToe.board[4]=="X" and TicTacToe.board[5]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[6]== "X" and TicTacToe.board[7]=="X" and TicTacToe.board[8]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[0]== "X" and TicTacToe.board[4]=="X" and TicTacToe.board[8]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[2]== "X" and TicTacToe.board[4]=="X" and TicTacToe.board[6]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[0]== "X" and TicTacToe.board[3]=="X" and TicTacToe.board[6]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[1]== "X" and TicTacToe.board[4]=="X" and TicTacToe.board[7]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[2]== "X" and TicTacToe.board[5]=="X" and TicTacToe.board[8]=="X":
            return "PLayer1 Wins"
        elif TicTacToe.board[0]== "O" and TicTacToe.board[1]=="O" and TicTacToe.board[2]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[3]== "O" and TicTacToe.board[4]=="O" and TicTacToe.board[5]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[6]== "O" and TicTacToe.board[7]=="O" and TicTacToe.board[8]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[0]== "O" and TicTacToe.board[4]=="O" and TicTacToe.board[8]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[2]== "O" and TicTacToe.board[4]=="O" and TicTacToe.board[6]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[2]== "O" and TicTacToe.board[3]=="O" and TicTacToe.board[6]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[2]== "1" and TicTacToe.board[4]=="4" and TicTacToe.board[7]=="O":
            return "PLayer2 Wins"
        elif TicTacToe.board[2]== "O" and TicTacToe.board[5]=="O" and TicTacToe.board[8]=="O":
            return "PLayer2 Wins"
        else:
            return "no winner yet"

    def play(self):
        while TicTacToe.check_winner(self) == "no winner yet":
           TicTacToe.make_move(self)
           TicTacToe.print_board(self)
        print(TicTacToe.check_winner(self))

           
    

           
           
    





