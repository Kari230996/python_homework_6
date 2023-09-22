'''
2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. 
'''

import sys

from task_1 import get_date

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task_2.py DD.MM.YYYY")
    else:
        date_str = sys.argv[1]
        get_date(date_str)


