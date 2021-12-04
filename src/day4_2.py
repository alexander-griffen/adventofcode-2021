import utils

day_input = utils.get_input()

drawn_numbers = day_input[0]

boards = []
new_board = []
for row in day_input[2:]:
    if row != '':
        new_board.append(row)
    else:
        boards.append(new_board)
        new_board = []
boards.append(new_board)

drawn_numbers = [int(i) for i in drawn_numbers.split(',')]

new_boards = []
for board in boards:
    new_board = []
    for row in board:
        new_board.append([int(i) for i in row.split()])
    new_boards.append(new_board)
boards = new_boards


def check_rows(board):
    for row in board:
        if row == [-1, -1, -1, -1, -1]:
            return True
    return False


def check_columns(board):
    # get list of columns
    columns = [[], [], [], [], []]
    for row in board:
        for i, number in enumerate(row):
            columns[i].append(number)

    for column in columns:
        if column == [-1, -1, -1, -1, -1]:
            return True
    return False


def check_winner(board):
    if check_rows(board) or check_columns(board):
        return True
    return False


def calculate_score(winning_board, number_called):
    numbers = []
    for row in winning_board:
        for i in row:
            if i != -1:
                numbers.append(i)
    return sum(numbers) * number_called


scores = []

for number in drawn_numbers:

    # Update the boards with the new scores
    new_boards = []
    for board in boards:
        new_board = board.copy()
        for i, row in enumerate(board):
            for j, board_number in enumerate(row):
                if number == board_number:
                    new_board[i][j] = -1
        new_boards.append(board)
    boards = new_boards

    # Check for winners in each board
    new_boards = []
    for board in boards:
        if check_winner(board):
            #If there is a winner, add the score to the list
            scores.append(calculate_score(board, number))
        else:
            # If the board isn't a winner, it's still in the playing
            new_boards.append(board)
    boards = new_boards

# Print the last score
print(scores[-1])
