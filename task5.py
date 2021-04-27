"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

import subprocess


def get_ping(tasks):
    for task in tasks:

        ping_process = subprocess.Popen(task, stdout=subprocess.PIPE)

        i = 0

        for line in ping_process.stdout:

            if i < 10:
                print(line)  # для наглядности ответ в байтах
                line = line.decode('cp866').encode('utf-8')
                print(line.decode('utf-8'))
                i += 1
            else:
                print('#' * 30)
                break


tasks = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
get_ping(tasks)
