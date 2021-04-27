"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import locale

lst = ['сетевое программирование', 'сокет', 'декоратор']

# file creation
with open('test_file.txt', 'w+') as f:
    for i in lst:
        f.write(i + '\n')
    f.seek(0)

print(f)  # print file object to get encoding type

file_coding = locale.getpreferredencoding()

# reading from file
with open('test_file.txt', 'r', encoding=file_coding) as f:
    for i in f:
        print(i)

    f.seek(0)
