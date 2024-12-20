class Person:
    university='Rajshahi University'
    def __init__(self,name,age):
     self.name=name
     self.age=age
    
    def greet(self):
        print(f'hello my name is {self.name} and i am {self.age} years old. ')

person1=Person('alice',25)
person1.greet()
person2=Person('bob',50)
person2.greet()
person3=Person('adam',20)
person3.greet()
                     
print(Person.university)
