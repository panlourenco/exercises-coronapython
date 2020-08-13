# 9.3 Users

class User():
    
    def __init__(self, first, last, address, age):
        self.first = first
        self.last = last
        self.address = address
        self.age = age

    def describe_user(self):
        print(self.first, self.last, self.address, self.age)
    
    def greet_user(self):
        print('Hi!, My name is  ' + self.first + '.' + ' I am glad to meet you! ')


john = User('Johnny', 'Depp','California',57)
john.describe_user()
john.greet_user()
bryan = User('Bryan', 'Cranston','California',64)
bryan.describe_user()
bryan.greet_user()
matthew = User('Matthew', 'McConaughey', 'Texas', 50)   
matthew.describe_user() 
matthew.greet_user()


