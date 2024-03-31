def set_method(any_set, operation):
    if operation[0] == "pop":
        return any_set.pop()
    elif operation[0] in ("remove", "discard"):
        return any_set.discard(operation[1])
    else:
        return "Некорректный ввод"


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    if len(s) <= n and all(0 <= num <= 9 for num in s):
        N = int(input())
        for _ in range(N):
            print(set_method(s, input().split()))
    else:
        print("Некорректный ввод чисел.")
