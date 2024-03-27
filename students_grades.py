if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    second_grade = list(set(sorted([grade[1] for grade in grades])))[1]
    for name in sorted([x[0] for x in grades if x[1] == second_grade]):
        print(name)
