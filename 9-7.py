class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + self.last_name

    def describe_user(self):
        print(self.name)

    def greet_user(self, word):
        print(self.name, str(word))


class Admin(User):
    def __init__(self, first_name,last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['add post', 'delete post']

    def show_privileges(self):
        print("This user can:")
        for one in self.privileges:
            print("\t", one)


me = Admin("尹","振宇")
me.show_privileges()
me.describe_user()