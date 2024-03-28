def split_and_join(line):
    splitted_str = line.split(" ")
    joined_str = "-".join(splitted_str)
    return joined_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
