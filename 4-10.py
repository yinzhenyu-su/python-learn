#切片
words=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('My word:',words[:3])
his_word=words[:]
words.append('z')
print(words)
his_word.append('y')
print(his_word)