from prettytable import PrettyTable  # Импортируем установленный модуль.
th = ['раздел ', 'его размер, байт', 'свободен']
td = ['1',          '16000',                'yes',
      '2',          '23000',               'yes',
      '3',          '15000',              'yes',
      '4',          '40000',              'yes',
      '5',          '30000',              'yes',
      '6',          '50000',              'yes']
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
    vib = int(input('  1 - add |      2 - start   | 3 - replace  >>  '))
    if vib == 1:
        filename = sg.popup_get_file('Добавьте файлы в очередь')
        a = a + 1
        colls.append('%6s' % str(a) + ' ')
        name = os.path.basename(filename)
        sizef = os.stat(filename).st_size
        size.append('%6s' % sizef + ' ')

        index = name.index('.')
        file.append('%6s' % name[:index]+ ' ')

    if vib== 3:
        vib2 = int(input('>> '))
        aa = colls.pop(vib2-1)
        colls.append(aa)
        bb = file.pop(vib2-1)
        file.append(bb)

    if vib ==2:
        i = 0
        prov2 = size.pop(0)
        colls.pop(0)
        file.pop(0)
        while i<len(td):
            prov3 = int(td[i+1])
            i+=3
            print(prov2, ' < ', prov3)
            if prov3 > int(prov2):
                print('yes')
            else:
                print('no')
    print(colls)
    print(file)
    print(size)













