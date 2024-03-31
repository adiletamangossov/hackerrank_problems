import string


def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    letters = alphabet[:size]
    if size == 1:
        print(alphabet[0])
    else:
        for i in range(size, 0, -1):
            print(
                ("-".join(letters[i:size][::-1]) +
                 "-"+letters[i-1]+"-" +
                 "-".join(letters[i:size])
                 ).center((size*2-1)*2-1, "-")
            )
        for i in range(2, size+1):
            print(
                ("-".join(letters[i:size][::-1]) +
                 "-" + letters[i - 1] + "-" +
                 "-".join(letters[i:size])
                 ).center((size * 2 - 1) * 2 - 1, "-")
            )


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
