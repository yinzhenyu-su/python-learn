#life's different stage
age=input('What age are you:')
age=int(age)
if age < 2:
    print('You Kidding?')
elif age in range(2,4):
    print('You are learning walk.')
elif age in range(4,13):
    print('You are kid.')
elif age in range(13,20):
    print('You are teen.')
elif age in range(10,65):
    print('You are adult.')
else:
    print('You are Old.')