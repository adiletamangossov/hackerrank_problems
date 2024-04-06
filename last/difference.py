def number_at_least_subscription(students1, students2):
    return len(set(set(students1).difference(students2)))


if __name__ == '__main__':
    n = int(input())
    en_students = input().split()
    b = int(input())
    fr_students = input().split()
    print(number_at_least_subscription(en_students, fr_students))
