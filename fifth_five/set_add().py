if __name__ == '__main__':
    countries = set()
    N = int(input())
    for _ in range(N):
        countries.add(input())
    print(len(countries))
