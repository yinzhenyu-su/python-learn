with open('learning_python.txt') as file_object:
    lines=file_object.readlines()
    text=''
    for line in lines:
        text+=line


text=text.replace('python','c')
print(text)