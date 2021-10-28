# 五香烟熏牛肉卖完了
sandwich_orders = ['pastrami', 'fish', 'pastrami', 'pastrami']
sandwich_orders.sort(reverse=False)
print('五香烟熏牛肉卖完了')
while 'pastrami' in sandwich_orders:
    sandwich_orders.pop()
print(sandwich_orders)
