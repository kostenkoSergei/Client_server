"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""
lst_bytes = [b'class', b'function', b'method']
for line in lst_bytes:
    print(f'тип переменной: {type(line)}\n')
    print(f'содержание переменной - {line}\n')
    print(f'длинна строки: {len(line)}\n')
