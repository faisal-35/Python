num=int(input('enter the num='))
if (num%2==0):
    print('the number is even ')
else:   
    print('the number is odd') 
if (num%3==0 and num%5==0):
    print(f'the number is divided by 3 and 5, \nthe  number is {num} ' )
else:
    print(f'the number is not divided by 3 and 5,\nthe number is {num}')
