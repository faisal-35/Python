def fibonacci(num):
 if num==0:
   return 0
 elif num==1:
   return 1
 else:
     return  fibonacci(num-1)+fibonacci(num-2)



n=int(input("enter the value :"))
if n<=0:
   print("Plese enter a positive integer")
else:
   print(f"First {n} Number Fibonacci sequence:")
   
   for i in range(n):
          print(fibonacci(i),end=',')
