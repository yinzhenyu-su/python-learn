# 请吃饭
names = ['吴炜', '李权', '董景祥', '我']
print('消息：')
for name in names:
    print('\t', name, '今天我请你吃饭')
# 修改名单
print('消息：')
print('\t', '今天', names.pop(), '有事', '去不了了')
names.append('吴炜2')
print('\t', '今天', names[3], '代替我请客', '你们找他')
print('消息：')
for name in names:
    print('\t', name, '今天', names[3], '请客吃饭')
print('消息：')
print('\t', names[3], '找到了一张大桌子，可以邀请更多的人')
# 添加名单
names.insert(0, '我')
names.insert(2, '我1')
names.append('我2')
print('消息：')
print('\t', names[5], '邀请了', names[0])
print('\t', names[5], '邀请了', names[2])
print('\t', names[5], '邀请了', names[-1])
print('消息：')
for name in names:
    print('\t', name, '今天', names[5], '请客吃饭')
# 缩减名单
print('消息：')
print('\t', '桌子没了', names[5], '只能请两个人吃饭了')
for name in names:
    if(len(names) > 1):
        print('\t', names.pop(), '抱歉,不能请你吃饭')
print('消息：')
for name in names:
    print('\t', name, '今天', names[1], '请客吃饭')
print('请客名单', names)
del names[2]
print('请客名单', names)
del names[1]
print('请客名单', names)
print('消息：')
for name in names:
    print('\t', name, '今天', name, '请客吃饭')
del names[0]
print('请客名单', names)
# 请客结束
