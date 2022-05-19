from prettytable import PrettyTable
import PySimpleGUI as sg
import os
th = ['раздел ', 'его размер, байт', 'свободен']
td = ['1',          '16000',                'yes',
      '2',          '5000',               'yes',
      '3',          '6000',              'yes',
      '4',          '10000',              'yes',
      '5',          '28000',              'yes']

file = []
colls = []
size = []
a = 0

while True:
    columns = len(th)  # Подсчитаем кол-во столбцов на будущее.
    table = PrettyTable(th)  # Определяем таблицу.
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)

    vib = int(input('  1 - add |      2 - start   | 3 - replace | 4 - выполнить | >>  '))
    if vib == 1:
        filename = sg.popup_get_file('Добавьте файлы в очередь')
        sizef = os.stat(filename).st_size
        if sizef > 28000:
            print('Невозможно добавить: размер задачи больше максимального размера раздела')
        else:
            a = a + 1
            colls.append('%6s' % str(a) + ' ')
            name = os.path.basename(filename)

            size.append('%6s' % sizef + ' ')

            index = name.index('.')
            file.append('%6s' % name[:index] + ' ')


    if vib== 3:
        vib2 = int(input('>> '))
        aa = colls.pop(vib2-1)
        colls.append(aa)
        bb = file.pop(vib2-1)
        file.append(bb)
        cc = size.pop(vib2-1)
        size.append(cc)
        vib2 = 0
    if vib== 4:
        vib2 = int(input('Номер задачи >> '))
        if vib2 !=1:
            if td[vib2+(vib2*2-1)] != 'yes':
                td[vib2 + (vib2 * 2 - 1)] = 'yes'
            else:
                print('раздел свободен')
        else:
            if td[2] != 'yes':
                td[2] = 'yes'
            else:
                print('раздел свободен')

    if vib ==2:
        print('running :\n', colls[0], '\n', file[0], '\n', size[0])
        i = 0
        triger = True
        schet= 65000
        scheti =0
        prov2 = size.pop(0)
        colls2 = colls.pop(0)
        name2 = file.pop(0)

        while i<len(td):
            prov3 = int(td[i+1])

            if prov3 > int(prov2):
                if prov3 < schet:
                    if td[i+2] == 'yes':
                        triger= False
                        schet = prov3
                        scheti = i+2
            i += 3
        if triger == False:
            td[scheti] = name2
        else:
            print('сейчас все подходящие разделы заняты, задача ставится в конец очереди')
            size.append(prov2)
            colls.append(colls2)
            file.append(name2)

    print('N    ' ,colls)
    print('name ',file)
    print('size ',size)















