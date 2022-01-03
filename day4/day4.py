from re import split


# Represents a bingo board.
class Board:
    def __init__(self, board):
        # Initialises self given a 2D list representation.
        self.board = board
        self.num_to_pos = {}
        self.unmarked = set()
        self.last_marked = ""

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                self.num_to_pos[n] = (i, j)
                self.unmarked.add((i, j))

    def mark(self, n):
        # Mark this board with n, and return True if successfully marked,
        # False otherwise.

        if not self.num_to_pos.get(n):
            # This board does not have n
            return False

        self.unmarked.remove(self.num_to_pos[n])
        self.last_marked = n
        return True

    def is_complete(self):
        # This is called every time a number is marked
        # Only need to check row, column of last marked position
        x, y = self.num_to_pos[self.last_marked]
        column_complete = True
        for col in range(len(self.board[x])):
            if (x, col) in self.unmarked:
                column_complete = False
                break

        if column_complete:
            return True

        for row in range(len(self.board)):
            if (row, y) in self.unmarked:
                return False

        return True

    def score(self):
        result = 0
        for x, y in self.unmarked:
            result += int(self.board[x][y])

        return int(self.last_marked) * result


# Return (bingo_nums, boards) where bingo_nums is a list of strings
# representing bingo numbers being called, and boards is a list of Boards.
def read_input(lines):
    boards = []
    i = 0
    while i < len(lines):
        line = lines[i][:-1]
        if i == 0:
            # First line is bingo numbers
            bingo_nums = line.split(",")
            i += 1
        elif line:
            # A bingo board
            board = []
            for j in range(i, i + 5):
                row = split(" +", lines[j][:-1])
                row = [n for n in row if n]
                board.append(row)

            i += 5
            boards.append(Board(board))
        else:
            i += 1

    return bingo_nums, boards


def predict_first_winning_score(lines):
    bingo_nums, boards = read_input(lines)
    for n in bingo_nums:
        for board in boards:
            if board.mark(n) and board.is_complete():
                return board.score()


def predict_last_winning_score(lines):
    bingo_nums, boards = read_input(lines)
    last_won = None
    for n in bingo_nums:
        # Filter out winning boards
        incomplete_boards = []
        for b in boards:
            if b.mark(n) and b.is_complete():
                last_won = b
            else:
                incomplete_boards.append(b)

        boards = incomplete_boards

    return last_won.score()


if __name__ == "__main__":
    lines = open("day4.txt", "r").readlines()
    print(predict_first_winning_score(lines))
    print(predict_last_winning_score(lines))

