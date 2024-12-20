def modify_immutable(x):
    x=10
    print('inside function' ,x)
a=5
modify_immutable(a)
print('outside function ',a)

def modify_mutable(lst):

   lst.append(5)
   print('inside function',lst)
 
my_list=[1,2,3]
modify_mutable(my_list)
print('outside funtion',my_list)   
   
