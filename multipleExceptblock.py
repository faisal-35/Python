try:
    
    x=int('abc')
         num=(12/0)
except ValueError:
    print('invalid input')
except ZeroDivisionError:
     print('division by zero error')
print("after exception clause")     
