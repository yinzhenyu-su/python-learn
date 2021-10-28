# 输出键值
favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c'],
    'edward': ['ruby'],
    'phil': ['python']
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:  # len()大于1遍历list
        print(name.title() + "'s favorite language are :")
        for language in languages:
            print(language)
    else:  # 否则直接输出
        print(name.title() + "'s favorite language are", languages[0])
