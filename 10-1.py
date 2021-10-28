with open('learning_python.txt') as file_object:
    content=file_object.read()
    print(content)


with open('learning_python.txt') as file_object:
    lines=file_object.readlines()
    for line in lines:
        print(line)


with open('learning_python.txt') as file_object:
    lines=file_object.readlines()
    text=[]
    for line in lines:
        text.append(line)
for line in text:
    print(line)