def huiwen_qiepian(word):
    new_list = word[::-1]
    if new_list == word:
        return True
    else:
        return False


def huiwen_digui(word):
    if len(word) == 0:
        return True
    else:
        if word[0] == word[-1]:
            return huiwen_digui(word[1:-1])
        else:
            return False


def print_all(word):
    print(huiwen_qiepian(word))
    print(huiwen_digui(word))


print_all('6666')
