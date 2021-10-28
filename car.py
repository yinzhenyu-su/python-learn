class Car():
    def __init__(self, make, model, year):
        """一次模拟汽车的简单尝试"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odcmeter(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer")


class E_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = E_Car("tesla", "model s", "2016")
print(my_tesla.get_descriptive_name())
