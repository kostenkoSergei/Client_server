"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
 формате и проверить тип и содержание соответствующих переменных. Затем с помощью
 онлайн-конвертера преобразовать строковые представление в формат Unicode и также
 проверить тип и содержимое переменных.
"""
lst_str = ['разработка', 'сокет', 'декоратор']

for line in lst_str:
    print(f'тип переменной: {type(line)}\n')
    print(f'содержание переменной - {line}\n')
    print(f'длинна строки: {len(line)}\n')

print("#" * 30)

lst_unicode = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
               b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
               b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for line in lst_unicode:
    print(f'тип переменной: {type(line)}\n')
    print(f'содержание переменной - {line}\n')
    print(f'длинна строки: {len(line)}\n')
