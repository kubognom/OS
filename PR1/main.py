import json
import os
import psutil



d = psutil.disk_partitions()
i = -1
for disk in psutil.disk_partitions():
    i += 1
    p = psutil.disk_usage(d[i][0])
    print('Название: ', d[i][0], '  Тип: ', d[i][3], ' Обьем: ', p[0] // (2 ** 30), ' Свободно: ', p[2] // (2 ** 30))

my_file = open("file.txt", "w+")
my_file.write(input("Введите строку для записи в файл >>  "))
my_file.close()
A = 0
while A != 4:
    A = int(input("1 -- удалить файл, 2 -- записать, 3 -- прочитать, 4 -- выйти\n>>  "))
    if A == 1:
        os.remove("file.txt")
        print("Файл успешно удален")
        A = 4
    elif A == 3:
        my_file = open("file.txt", "r")
        print(my_file.read())
        A = 0
    elif A == 2:
        my_file = open("file.txt", "a+")
        my_file.write("  " + input("Введите строку для записи в файл >>  "))
        A = 0
    my_file.close()
data = {}
data['people'] = []
A = int(input("Сколько записать человек? >> "))
for i in range(A):
    print(i + 1, "й человек")
    data['people'].append({
        'name': input(" Имя >> "),
        'website': input(" Сайт  >> "),
        'from': input(" Место >> ")
    })

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
outfile.close()
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
json_file.close()
A = 0
while A != 4:
    A = int(input("1 -- удалить json, 2 -- записать json, 3 -- прочитать json, 4 -- выйти\n>>  "))
    if A == 1:
        os.remove("data.json")
        print("Файл успешно удален")
        A = 4
    elif A == 3:
        with open('data.json') as json_file:
            data = json.load(json_file)
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')
        A = 0
    elif A == 2:
        A = int(input("Сколько записать человек? >> "))
        for i in range(A):
            print(i + 1, "й человек")
            data['people'].append({
                'name': input(" Имя >> "),
                'website': input(" Сайт  >> "),
                'from': input(" Место >> ")
            })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()
        A = 0
    json_file.close()
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "journal")
A = input("Сколько людей записать в XML? >> ")
for i in range(int(A)):
    ET.SubElement(doc, "HumanN" + str(i + 1), name=input(('Имя cотрудника >> '))).text = input(("Номер телефона >> "))

tree = ET.ElementTree(root)
tree.write("filename.xml")

i2 = 0
for elem in root:
    print('<', root.tag, '>', '\n   <', elem.tag, '>')
    for subelem in elem:
        i2 += 1
        print('    <', subelem.tag, subelem.attrib, '> ', subelem.text, '</', subelem.tag, '>')
    print('   </', elem.tag, '>', '\n</', root.tag, '>')

A = 0
while A != 4:
    A = int(input("1 -- удалить XML, 2 -- записать XML, 4 -- выйти\n>>  "))
    if A == 2:
        A = input("Сколько людей записать в XML? >> ")
        for i in range(int(A)):
            tree = ET.parse('filename.xml')
            root = tree.getroot()
            element = root[0]
            ET.SubElement(element, "HumanN" + str(i2 + i + 1), name=input(('Имя cотрудника >> '))).text = input(
                ("Номер телефона >> "))
            tree.write("filename.xml")
        i2 = 0
        for elem in root:
            print('<', root.tag, '>', '\n   <', elem.tag, '>')
            for subelem in elem:
                i2 += 1
                print('    <', subelem.tag, subelem.attrib, '> ', subelem.text, '</', subelem.tag, '>')
            print('   </', elem.tag, '>', '\n</', root.tag, '>')
            A = 0
    if A == 1:
        os.remove("filename.xml")
        print("XML deleted")
        A = 4

dirname = '/Users/Nikta/PycharmProjects/pythonProject/PR1'
files = os.listdir(dirname)
print(files)
import zipfile
archive = zipfile.ZipFile('Archive.zip', mode='w')
A = int(input('какой из файлов добавить в архив?(номер) >>  '))
archive.write(files[A-1])
os.remove(files[A-1])
print('файлы добавлены')
archive.close()
archive = zipfile.ZipFile('Archive.zip', 'r')
archive.extractall('.')
print('Распаковано')
for ar in archive.infolist():
    print(ar.filename, '|Дата создания: ', ar.date_time[0],ar.date_time[1],ar.date_time[2],'|Размер: ', ar.file_size)
archive.close()
os.remove("Archive.zip")