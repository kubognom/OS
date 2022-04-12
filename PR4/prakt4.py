from datetime import datetime

a=0
b=3
c =3
i1 =0
i = 100000000
start_time = datetime.now()

while i1 < i:
    a += b*2 + c - i1
    i1+=1

print('Время  = ', datetime.now() - start_time, '\n',a)