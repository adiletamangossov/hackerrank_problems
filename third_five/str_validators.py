if __name__ == '__main__':
    s = input()
    print(sum([letter.isalnum() for letter in s]) > 0)
    print(sum([letter.isalpha() for letter in s]) > 0)
    print(sum([letter.isdigit() for letter in s]) > 0)
    print(sum([letter.islower() for letter in s]) > 0)
    print(sum([letter.isupper() for letter in s]) > 0)
