
l1=[3,6,9,12,15,18,21]

l2=[4,8,12,16,20,24,28]
l3=[]

print("Elements at the list L1:",end='')
print(l1)
print("Elements at the list L2:",end='')
print(l2)
print("Elements at odd index positions from the list L1:",end='')
print(l1[1::2])
print("Elements at odd index positions from the list L2:",end='')
print(l2[::2])

for i in l1[1::2]:
  l3.append(i)

for i in l2[::2]:
  l3.append(i)

print("The final  list L3:",end='')
  
print(l3)


