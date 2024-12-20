 
list=[e**2 for e in range(1,6)]
print(list)
list1=[e**2 for e in range(1,7) if e%2==0]
print(list1)
list2=[(e,e**2) for e in range(1,7) if e%2==1]
print(list2)
list3=[x for x in range(50) if '7' in str(x)]
print(list3)
  
