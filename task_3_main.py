from task_3_chess_utils import is_safe

def solve_queens(board):
    if is_safe(board):
        return True
    return False

if __name__ == '__main__':
    queens = []

    for _ in range(8):
        row, col = map(int, input("Введите координаты ферзей (ряд столбец): ").split())
        queens.append(col)

    if solve_queens(queens):
        print('Ферзи не бьют друг друга. :)')
    else:
        print('Ферзи бьют друг друга. :(')

