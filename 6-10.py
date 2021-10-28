#favorite number
active_flag=True
li=[]
dic={}

while active_flag:
    repeat=print("you can quit at anytime with 'quit/q'".title())
    name=input('please tell me your name:'.title())
    number=input('please tell me your favorite number:'.title())
    
    li.append(dic)
    if name=='q' or number=='q':
        active_flag=False
    else:
        number=int(number)
        dic['name']=name
        dic['number']=number
        repeat
for l in li:
    print(l)
    