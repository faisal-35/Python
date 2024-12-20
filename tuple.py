my_list=[0,1,2,3,4,5]
my_tuple=(0,1,2,3,4,5,6)

print(f'my_list = {my_list[:]}')
print(f'my_tuple = {my_tuple[:]}\n')
print('omiting start and stop')

print(f'my_list = {my_list[:]}')
print(f'my_tuple = {my_tuple[:]}\n')


print('basic slicing')
print(f'my_list = {my_list[:4]}')
print(f'my_tuple = {my_tuple[:4]}\n')
print('omitingn start')
print(f'my_list = {my_list[1:4]}')
print(f'my_tuple = {my_tuple[1:4]}\n')
print('use step 2')
print(f'my_list = {my_list[2::2]}')
print(f'my_tuple = {my_tuple[::2]}\n')
print('negative index')
print(f'my_list = {my_list[-6:-1]}')
print(f'my_tuple = {my_tuple[-7:-1:2]}\n')



