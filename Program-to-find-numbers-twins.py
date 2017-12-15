print('Эта программа ищет простые числа-близнецы в диапазоне от 1 до n.')
n = int(input("n="))

if n>=10000:
    print('Дай-ка подумать...')
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

pp=len(lst2)
print('В диапазоне от 1 до %s обнаружено %s пар чисел-близнецов. Вот они%s:' %(n,pp,fur))
print(lst2)
