print('Эта программа ищет простые числа-близнецы в диапазоне от 1 до n.')

while True:
    try:
        n = input("n=")
        n1=int(n)
        n=n1
        break
    except(ValueError):
        try:
            n2=float(n)
            n=n2
            n=int(n)
            print('Вы ввели вещественное число, округляем его до целого.')
            break
        except(ValueError):
            print('Вы ввели не число, давайте-ка попробуем снова.')

if n>=10000:
    print('Дайте-ка подумать...')
if n==1488:
    fur=', фюрер'
elif n==666:
    fur=', Царь Преисподней'
elif n==123 or n==1234 or n==12345 or n==123456 or n==1234567 or n==12345678 or n==123456789 or n==1234567890 or n==1111:
    fur=', Basic-man'
else:
    fur=''

lst = []
lst2=[]
n3=n+1

for i in range(2,n3):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)

ff=None

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
