from prettytable import PrettyTable  # Импортируем установленный модуль.
th = ['раздел ', 'его размер, байт', 'свободен']
td = ['1',          '16 000',                'yes',
      '2',          '23 000',               'yes',
      '3',          '15 000',              'yes']
columns = len(th)  # Подсчитаем кол-во столбцов на будущее.
table = PrettyTable(th)  # Определяем таблицу.
td_data = td[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
print(table)
file = []
colls = []
size = []
a = 0
import PySimpleGUI as sg
import os
while True:
    vib = int(input('1 - add | 2 - start | 3 - replace  >>  '))
    if vib == 1:
        filename = sg.popup_get_file('Добавьте файлы в очередь')
        a = a + 1
        colls.append('%6s' % str(a) + ' ')
        name = os.path.basename(filename)
        sizef = os.stat(filename).st_size
        size.append('%6s' % sizef + ' ')

        index = name.index('.')
        file.append('%6s' % name[:index]+ ' ')
        print(colls)
        print(file)
        print(size)
    if vib== 3:
        vib2 = int(input('>> '))
        aa = colls.pop(vib2-1)
        colls.append(aa)
        bb = file.pop(vib2-1)
        file.append(bb)
        print(colls)
        print(file)










