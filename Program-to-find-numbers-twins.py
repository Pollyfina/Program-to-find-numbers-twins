
# coding: utf-8

# In[ ]:


print('Эта программа генерирует прочтые числа близнецы в диапазоне от 1 до n.')
n = int(input("n="))
lst = []
lst2=[]
y=n+1

for i in range(2,y):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)

for bliz in range (len(lst)):
    for bliz2 in range(len(lst)):
        if bliz2 != len(lst)-1:
            ff=lst[bliz]-2
            kk=ff+2
    for bliz3 in range(len(lst)):
        if ff==lst[bliz3]:
            lst2.append(ff)
            lst2.append(kk)
print(lst2)

