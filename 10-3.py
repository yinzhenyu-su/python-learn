p = input("请输入你的名字，它会被保存到文件中：")

with open('name.txt', 'w', encoding='utf-8') as file_object:
    file_object.write(p)
    print('文件已保存')
