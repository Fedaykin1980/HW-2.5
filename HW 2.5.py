import random
import datetime


class MyOpen:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def game(): #Игра в которой компьютер угадавает число, загаданное пользователем
    print('Загадайте число от 1 до 10')
    min_number = 1
    max_number = 10
    result = None

    while result != '=':
        number = random.randint(min_number, max_number)
        print(number)
        result = input('Введите знак по отношению к задуманному числу: < > =')
        if result == '<':
            min_number = number + 1
        elif result == '>':
            max_number = number - 1
    print('Число угадано!')


if __name__ == '__main__':
    with MyOpen('test.txt') as f:
        start_time = datetime.datetime.now()
        f.write(str(start_time) + '\n')
        game()
        end_time = datetime.datetime.now()
        f.write(str(end_time) + '\n')
        delta = end_time - start_time
        f.write(str(delta) + '\n')

        print(f'Время начала работы программы: {start_time}')
        print(f'Время окончания работы программы: {end_time}')
        print(f'Общее время работы программы: {delta}')