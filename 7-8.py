sandwich_orders=['fish','butter','chicken']
maded=[]
while sandwich_orders:
    for sandwich in sandwich_orders:
        print('i made you a '+sandwich+' sandwich.')
        maded.append(sandwich_orders.pop())
print('sandwich_orders:',sandwich_orders)
for made in maded:
    print('this is maded:'.title(),made)