#problem 01
import array as ar
a=ar.array('i',[10,20,30,40,50])
print(a)
a.insert(1,60);
print('a new element 60 between 10 and 20:')
for i in a:
    print(i)
print(a)
print('delete an element at index 3:')
del a[3];
print(a)
print('search an element:')
x=int(input('enter the search element:'))
for j in a:
    if j==x:
        print ('found the element which is:',x)
        break
    else:
        print ('not found the element ')
#problem o2       
print('found the even number :')        
b=ar.array('i',[10,5,15,4,6,20,9])
c=ar.array('i',[])
print(b)
print('the even number is:')
for i in b:
    if i%2==0:
        c.append(i)
        
print(c)        
        
