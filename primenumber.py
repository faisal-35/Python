def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num*.5)+1):
       if num%i==0:
        return False
    return True
for n in range(10,50):
    if not is_prime(n):
      continue
    print(f'the first prime number is found {n}')
    
 
