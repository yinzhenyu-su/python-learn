from random import *


def get_num():
    a = randint(0, 100)
    return a


def guess(num):
    # judge the parameter
    raw_input = input()

    if raw_input == "n":
        print("Well,Bye.")
        return 88
    else:
        try:
            x = int(raw_input)
        except ValueError as e:
            print("Please give me a number:(n for exit)")
            return guess(num)

        if x > num:
            return 1
        elif x < num:
            return -1
        else:
            return 0


def run():
    a = get_num()
    print("I'm thinking a number from 0 to 100,can you guess it?(n for exit)")
    go = True
    while go:
        answer = guess(a)
        if answer == -1:
            print("No,the number i think was bigger.")
        elif answer == 1:
            print("No.the number i think was smaller")
        elif answer == 88:
            go = False
            continue
        elif answer == 0:
            print("Bingo,you got the number.")
            choose = input("continue?(y/n)")
            if choose == "y":
                run()
            else:
                go = False
                continue


if __name__ == '__main__':
    run()
