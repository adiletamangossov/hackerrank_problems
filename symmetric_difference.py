def sym_diff(x, y):
    new_set = x.difference(y).union(y.difference(x))
    return sorted(new_set)


if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))
    symmmetric_difference = sym_diff(a, b)
    for num in symmmetric_difference:
        print(num)
