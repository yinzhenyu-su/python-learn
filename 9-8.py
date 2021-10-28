class Privileges():
    def __init__(self, privi=['']):
        self.privileges = privi

    def show_privileges(self):
        for one in self.privileges:
            print("This user can", one)


pri = Privileges(['add post', 'delete post'])
pri.show_privileges()
