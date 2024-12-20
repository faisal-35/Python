fruits = ("apple","banana","cherry")
numbers = tuple(range(1,6))
nested_tuple =(fruits,numbers)
print(nested_tuple)


#task2
print(fruits[0])
print(numbers[-1])
print(nested_tuple[1])
print(nested_tuple[1][0])

#task3
a_tuple = ("orange","grape")
new_tuple = fruits+a_tuple
numbers2 = numbers*3
if("banana" in fruits):
    print("yes")


#task4
print(len(numbers))
print('max',max(numbers),'min', min(numbers))
print(list(numbers))

#task5
student= ("John Doe",21,"Computer Science")
print("Name of the student: ",student[0])
student_list =list(student)
student_list[1] = 22
student = tuple(student_list)
print(student)
