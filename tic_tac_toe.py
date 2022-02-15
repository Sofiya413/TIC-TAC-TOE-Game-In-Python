class Player:
    def __init__(self):
        self.p1 = "X"
        self.p2 = "O"
        self.matrix = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.i = []

    def player1(self):
        start = 0
        stop = 9
        print('\n\t\tTIC TAC TOE')
        print('\t\t~~~~~~~~~~~\n')
        print('Player 1 (X) & Player 2 (O)\n')
        print(1, '|', 2, '|', 3)
        print('----------')
        print(4, '|', 5, '|', 6)
        print('----------')
        print(7, '|', 8, '|', 9)
        for x in range(start, stop):
            if x % 2 == 0:
                self.play()
            if x % 2 == 1:
                self.player2()

        if self.matrix[0] == 'X' and self.matrix[1] == 'X' and self.matrix[2] == 'X':
            print('')
        elif self.matrix[3] == 'X' and self.matrix[4] == 'X' and self.matrix[5] == 'X':
            print(' ')
        elif self.matrix[6] == 'X' and self.matrix[7] == 'X' and self.matrix[8] == 'X':
            print(' ')
        elif self.matrix[0] == 'X' and self.matrix[3] == 'X' and self.matrix[6] == 'X':
            print(' ')
        elif self.matrix[1] == 'X' and self.matrix[4] == 'X' and self.matrix[7] == 'X':
            print(' ')
        elif self.matrix[2] == 'X' and self.matrix[5] == 'X' and self.matrix[8] == 'X':
            print(' ')
        elif self.matrix[0] == 'X' and self.matrix[4] == 'X' and self.matrix[8] == 'X':
            print(' ')
        elif self.matrix[6] == 'X' and self.matrix[4] == 'X' and self.matrix[2] == 'X':
            print(' ')
        else:
            print('\nMATCH DRAW!\n')
            self.gameover()

    def play(self):
        print('\n')
        row = int(input("Player 1, It is X's turn : "))
        if self.matrix[row - 1] != "X" and self.matrix[row - 1] != "O":
            self.i.append(row)
            self.matrix[row - 1] = 'X'
            print('\n')
            print(self.matrix[0], '|', self.matrix[1], '|', self.matrix[2], '\t', 1, '|', 2, '|', 3)
            print('----------')
            print(self.matrix[3], '|', self.matrix[4], '|', self.matrix[5], '\t', 4, '|', 5, '|', 6)
            print('----------')
            print(self.matrix[6], '|', self.matrix[7], '|', self.matrix[8], '\t', 7, '|', 8, '|', 9)
            if self.matrix[0] == 'X' and self.matrix[1] == 'X' and self.matrix[2] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[3] == 'X' and self.matrix[4] == 'X' and self.matrix[5] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[6] == 'X' and self.matrix[7] == 'X' and self.matrix[8] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[0] == 'X' and self.matrix[3] == 'X' and self.matrix[6] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[1] == 'X' and self.matrix[4] == 'X' and self.matrix[7] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[2] == 'X' and self.matrix[5] == 'X' and self.matrix[8] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[0] == 'X' and self.matrix[4] == 'X' and self.matrix[8] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
            elif self.matrix[6] == 'X' and self.matrix[4] == 'X' and self.matrix[2] == 'X':
                print('\nWinner is Player 1. ')
                obj.gameover()
        else:
            print('\nBox', row, 'is already filled.\nPlease enter the number of unfilled box.')
            self.play()

    def player2(self):

        print('\n')
        row = int(input("Player 2, It is O's turn : "))
        if self.matrix[row - 1] != "X" and self.matrix[row - 1] != "O":
            self.i.append(row)
            self.matrix[row - 1] = 'O'
            print('\n')
            print(self.matrix[0], '|', self.matrix[1], '|', self.matrix[2], '\t', 1, '|', 2, '|', 3)
            print('----------')
            print(self.matrix[3], '|', self.matrix[4], '|', self.matrix[5], '\t', 4, '|', 5, '|', 6)
            print('----------')
            print(self.matrix[6], '|', self.matrix[7], '|', self.matrix[8], '\t', 7, '|', 8, '|', 9)
            if self.matrix[0] == 'O' and self.matrix[1] == 'O' and self.matrix[2] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[3] == 'O' and self.matrix[4] == 'O' and self.matrix[5] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[6] == 'O' and self.matrix[7] == 'O' and self.matrix[8] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[0] == 'O' and self.matrix[3] == 'O' and self.matrix[6] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[1] == 'O' and self.matrix[4] == 'O' and self.matrix[7] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[2] == 'O' and self.matrix[5] == 'O' and self.matrix[8] == 'O':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[0] == 'X' and self.matrix[4] == 'X' and self.matrix[8] == 'X':
                print('\nWinner is Player 2. ')
                obj.gameover()
            elif self.matrix[6] == 'X' and self.matrix[4] == 'X' and self.matrix[2] == 'X':
                print('\nWinner is Player 2. ')
                obj.gameover()
        else:
            print('\nBox', row, 'is already filled.\nPlease enter the number of unfilled box.\n')
            self.player2()

    def gameover(self):
        for y in self.i:
            self.matrix[y - 1] = ' '

        again = input('\nWould you like to play again?? (Y OR N)  ')
        if again == 'y' or again == 'Y':
            self.player1()
        elif again == 'N' or again == 'n':
            exit('\nGame Over!')
        else:
            print('Please enter valid character.')


obj = Player()
obj.player1()
obj.gameover()
