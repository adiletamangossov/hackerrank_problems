import textwrap


def wrap(string, max_width):
    return textwrap.wrap(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for word in result:
        print(word)
