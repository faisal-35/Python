weight=float(input('Enter the weight of persel in kg :'))

if (0<weight<.1):
    print('shiping cost is 1$ ')
elif(.1<=weight<=5):
    print('shiping cost is 5$')
elif(5<weight<=10):
    print('shiping cost is 10$')
elif(10<weight<=15):
    print('shiping cost is 15$')
elif(15<weight<20):
    print('shiping cost is 20$')
else:
     print('not supported for shipping')
