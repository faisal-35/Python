numbers=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
result=[]
for list in numbers:
    squares=[number**2 for number in list if number%2==0]
    result.extend(squares)
 
print( result)
