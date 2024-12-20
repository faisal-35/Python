def is_prime(n)->bool:
   if n in[2,3]:
      return True
   if (n==1) or (n%2==0):
       return False
   r=3
   while r*r<=n:
        if n%r==0:
            return False
        r=r+2
   return True
"""prime_flag:bool
num:int"""
num=int(input('enter the number :'))
prime_flag=is_prime(num)
if(prime_flag==True):
    print('the number is prime')
else:
    print('the number is not prime')

   
     
