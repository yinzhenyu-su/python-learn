class Restaurant():
    """餐馆"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("name:",self.name)
        print("type:",self.cuisine_type)

    def open_restaurant(self):
        print(self.name, "开始营业了")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        if increment_number >= 0:
            self.number_served += increment_number
        else:
            print("increment_number should be real.")

