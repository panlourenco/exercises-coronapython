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
