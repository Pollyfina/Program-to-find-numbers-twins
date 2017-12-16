print('Эта программа ищет простые числа-близнецы в диапазоне от 1 до n.')

r=0
while r != 1:
    try:
        n = input("n=")
        o1=int(n)
        r=1
        n=o1
    except(ValueError):
        try:
            o2=float(n)
            r=1
            n=o2
            print('Вы ввели вещественное число, округляем его до целого.')
            n=int(n)
        except(ValueError):
            print('Вы ввели не число, давайте-ка попробуем снова.')

if n>=10000:
    print('Дайте-ка подумать...')
if n==1488:
    fur=', фюрер'
else:
    fur=''

lst = []
lst2=[]
y=n+1

for i in range(2,y):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)

for bliz in range (2,len(lst)):
    for bliz2 in range(2,len(lst)):
        if bliz2 != len(lst)-1:
            ff=lst[bliz]-2
            kk=ff+2
    for bliz3 in range(len(lst)):
        if ff==lst[bliz3]:
            oo='(%s + %s)' %(ff, kk)
            lst2.append(oo)

print('В диапазоне от 1 до %s обнаружено %s пар чисел-близнецов. Вот они%s:' %(n,len(lst2),fur))
print(lst2)

final=input()
while final != '':
    print('Для выхода из программы нажмите Enter.')
    final=input()
    if final=='':
        break
