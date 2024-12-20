#1.basic square
list=[x*x for x in range(1,11)]
print('a list of squares for numbers from 1 to 10 :')
print(list)



#even numbers
list1=[x for x in range(1,21) if x%2==0]
print('a list of even numbers from 1 to 20 :')
print(list1)



#string to upper case
fruit=['apple','banana','cherry']
print(f'list of string :{fruit}')
for i in range(3):
 fruit[i]=fruit[i].upper()
print('list of string uppercase :',fruit)


