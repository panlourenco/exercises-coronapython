# 9.5 Login Attempts

class User():
    
    def __init__(self, first, last, address, age):
        self.first = first
        self.last = last
        self.address = address
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.first, self.last, self.address, self.age)
    
    def greet_user(self):
        print('Hi!, My name is  ' + self.first + '.' + ' I am glad to meet you! ')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

john = User('Johnny', 'Depp','California',57)
john.describe_user()
john.greet_user()
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(john.login_attempts)
john.reset_login_attempts()
print(john.login_attempts)