'''
4. Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
from task_3_chess_utils import is_safe_2
from random import randint


def random_queens(board):
    if is_safe_2(board):
        return True
    else:
        return False


if __name__ == '__main__':
    successful_arrangements = []   # Здесь будем хранить успешные расстановки

    attempts = 0  # Счетчик попыток
    max_attempts = 100000  # Максимальное количество попыток

    # Ограничиваем количество попыток
    while len(successful_arrangements) < 4 and attempts < max_attempts:
        queens = []
        for _ in range(8):
            row = randint(1, 8)
            col = randint(1, 8)
            queens.append((row, col))

        if random_queens(queens):     # Проверяем, является ли расстановка успешной
            # Добавляем успешную расстановку в список
            successful_arrangements.append(queens)
        attempts += 1

    if successful_arrangements:
        for i, arrangement in enumerate(successful_arrangements, 1):
            print(f'Успешная растановка {i}:')
            for j, (row, col) in enumerate(arrangement, 1):
                print(f"Ферзь {j}: Ряд {row}, Столбец {col}")
            print()
    else:
        print("Не удалось найти успешные расстановки.")
