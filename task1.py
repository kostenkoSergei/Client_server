import csv
import re


def get_data(lst):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    producer = 'Изготовитель системы:'
    name = 'Название ОС:'
    code = 'Код продукта:'
    system = 'Тип системы:'
    for file in lst:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if re.search(producer, line):
                    os_prod_list.append(line.replace(producer, '').strip())
                if re.search(name, line):
                    os_name_list.append(line.replace(name, '').strip())
                if re.search(code, line):
                    os_code_list.append(line.replace(code, '').strip())
                if re.search(system, line):
                    os_type_list.append(line.replace(system, '').strip())
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    main_data.extend([os_prod_list, os_name_list, os_code_list, os_type_list])
    return main_data


def write_to_csv(file_name, lst):
    data = get_data(lst)
    with open(file_name, 'w', encoding='cp1251') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(data[0])
        for idx in range(len(data) - 1):
            if idx == 0:
                continue
            f_writer.writerow([data[1][idx - 1], data[2][idx - 1], data[3][idx - 1], data[4][idx - 1]])


if __name__ == '__main__':
    file_lst = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    write_to_csv('report.csv', file_lst)
