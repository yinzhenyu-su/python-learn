import json


filename = 'favnum.json'


def write_num():
    with open(filename, 'w') as file_obj:
        fav_num = input('please input your fav num:')
        json.dump(fav_num, file_obj)
        print('Done')


def read_num():
    with open(filename, 'r') as file_obj:
        content = json.load(file_obj)
        print('your fav num is:',content)


try:
    read_num()

except json.decoder.JSONDecodeError:
    print('空文件')
    write_num()

except FileNotFoundError:
    print('文件不存在')
    write_num()
