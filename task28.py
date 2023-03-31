# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

from task27 import file_generator as fg
import random

list_expansion = ['txt', 'csg', 'pdf', 'mp3', 'doc']
COUNT = 20


def file_generator2(list_exp: list[str], file_amount: int) -> None:
    list_amount = []
    up_bound = file_amount // len(list_exp)
    for i in range(len(list_exp) - 1):
        list_amount.append(random.randint(3, up_bound))
    list_amount.append(file_amount - sum(list_amount))
    for i in range(len(list_exp)):
        fg(list_exp[i], file_count=list_amount[i])


if __name__ == '__main__':
    file_generator2(list_expansion, COUNT)
