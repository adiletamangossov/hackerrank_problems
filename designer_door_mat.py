N, M = map(int, input().split())
if (N % 2 != 0) and (M / N == 3):
    figure = ".|."
    for i in range(N // 2):
        print((figure*i).rjust(M//2-1, "-") + figure + (figure*i).ljust(M//2-1, "-"))
    print("WELCOME".center(M, "-"))
    for i in range(N // 2, 0, -1):
        print((figure*i).rjust(M//2-1, "-") + figure + (figure*i).ljust(M//2-1, "-"))
else:
    print("Input odd number!")