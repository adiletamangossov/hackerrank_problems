def print_formatted(number):
    space = len(str(bin(number))[2:])+1
    for row in range(1, number+1):
        for col in range(1, 5):
            if col == 2:
                print(oct(row)[2:].rjust(space), end="")
            elif col == 3:
                print(hex(row)[2:].upper().rjust(space), end="")
            elif col == 4:
                print(bin(row)[2:].rjust(space), end="")
            else:
                print(str(row).rjust(space-1), end="")
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
