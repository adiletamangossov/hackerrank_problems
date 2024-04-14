def str_to_dict(string):
    return {i: string.count(i) for i in string}


if __name__ == '__main__':
    word = input()
    print(str_to_dict(word))
