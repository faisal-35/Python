#default argumrnts
def myfun(x,y=50):
    print('x:',x)
    print('y:',y)

myfun(20)
#keyword arguments
def student(firstname,lastname):
     print(firstname,lastname)

student(firstname='alice',lastname='lin')
student(lastname='lin',firstname='alice')

#positional arguguments
def add_num(a,b):
    c=a+b
    return c

result=add_num(10,20)
print(result)
 
#

