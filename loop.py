start=int(input('enter the start value='))
stop=int(input('enter the stop value='))
step=int(input('enter the step value='))
r=range(start,stop,step)
for i in r :
    val=r[-1]
    if i==val:
         print(i)
    else:
         print( i,end=',')


