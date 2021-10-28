with open('guest_book.txt','a',encoding='utf-8') as file_object:
    for time in range(3):
        p=input('请输入你的名字:')
        file_object.write(p+"\n")
        print('文件已保存')
