class TicTacGame:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def show_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def validate_input(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Некорректные координаты.")
            return False
        if self.board[row][col] != ' ':
            print("Ячейка уже занята.")
            return False
        return True

    def start_game(self):
        while True:
            self.show_board()
            print(f"Ходит игрок {self.current_player}")
            row = int(input("Введите номер строки (0, 1, 2): "))
            col = int(input("Введите номер столбца (0, 1, 2): "))

            if not self.validate_input(row, col):
                continue

            self.board[row][col] = self.current_player

            if self.check_winner():
                self.show_board()
                print(f"Игрок {self.current_player} победил!")
                break

            if all(cell != ' ' for row in self.board for cell in row):
                self.show_board()
                print("Ничья!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
