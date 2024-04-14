def lists_to_dict(lst1, lst2):
    return dict(zip(lst1, lst2))


if __name__ == '__main__':
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]
    print(lists_to_dict(list1, list2))
