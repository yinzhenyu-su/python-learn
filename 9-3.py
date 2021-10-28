class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.name=self.first_name+self.last_name
    def describe_user(self):
        print(self.name)
    def greet_user(self,word):
        print(self.name,str(word))

lq=User("李","权")
lq.describe_user()
lq.greet_user("Hello")

ww=User("吴","玮")
ww.describe_user()
ww.greet_user("Bay")