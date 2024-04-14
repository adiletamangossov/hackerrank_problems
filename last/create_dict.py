def create_dict(start, end):
    return {i: i ** 3 for i in range(start, end+1)}


if __name__ == '__main__':
    n_start = int(input())
    n_end = int(input())
    print(create_dict(n_start, n_end))
