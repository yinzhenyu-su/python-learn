from random import randint


class Die():
    """色子"""

    def __init__(self, sides=6):
        """默认六个面"""
        self.sides = sides

    def roll_die(self):
        """摇色子"""
        x = randint(1, self.sides)
        return x


# 6面
my_die = Die()
for time in range(10):
    print("\t", str(my_die.roll_die()))
# 10面
my_die1 = Die(10)
for time in range(10):
    print(str(my_die1.roll_die()))
# 20面
my_die2 = Die(20)
for time in range(10):
    print("\t", str(my_die2.roll_die()))
