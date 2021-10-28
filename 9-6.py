from restaurants import Restaurant


class IceCraemStand(Restaurant):
    def __init__(self, name, cuisine_type="ICE"):
        super().__init__(name, cuisine_type)
        self.flavors = ['a', 'b', 'c']

    def show_flavors(self):
        print("flavors:")
        for one in self.flavors:
            print("\t", one)


ice = IceCraemStand("ice")
ice.describe_restaurant()
ice.show_flavors()
