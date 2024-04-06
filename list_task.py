if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        action = input()
        if action.split()[0] == "insert":
            lst.insert(int(action.split()[1]), int(action.split()[2]))
        elif action == "print":
            print(lst)
        elif action.split()[0] == "remove":
            lst.remove(int(action.split()[1]))
        elif action.split()[0] == "append":
            lst.append(int(action.split()[1]))
        elif action == "sort":
            lst.sort()
        elif action == "pop":
            lst.pop()
        else:
            lst.reverse()
