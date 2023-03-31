# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from pathlib import Path
from task27 import file_generator as fg

string_dir = 'new_dir'


def file_generator3(path_string: str, expansion: str, file_count: int) -> None:
    name_list = os.listdir()
    dir_list = []
    for i in name_list:
        if os.path.isdir(i):
            dir_list.append(i)

    if path_string not in dir_list:
        print(Path.cwd())
        Path(path_string).mkdir()
    os.chdir(path_string)
    fg(expansion, file_count=file_count)


if __name__ == '__main__':
    file_generator3(string_dir, 'txt', 3)
