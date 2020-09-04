from user import User

class Privileges():
    def __init__(self):
        self.privileges = ("can add post", "can delete post", "can ban user")

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first, last, address, age):
        super().__init__(first, last, address, age)
        self.privileges = Privileges()

