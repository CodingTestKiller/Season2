from sys import stdin

input = stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    wishes = [0] + [int(x) for x in input().split()]

    teamed_students = set()
    students = set(range(1, m + 1))

    while students:
        student = students.pop()
        team = {student}
        wish = student

        if wishes[wish] == student:
            teamed_students.update(team)
            continue

        while students:
            # print(students, teamed_students, team, wish)
            if wishes[wish] == wish:
                teamed_students.update({wish})
                students.difference_update({wish})
                students.difference_update(team)
                break
            wish = wishes[wish]
            if wish == student:
                teamed_students.update(team)
                students.difference_update(team)
                break
            elif wish in teamed_students or wish not in students:
                break
            elif wish in team:
                tmp = student
                while tmp != wish:
                    team.remove(tmp)
                    tmp = wishes[tmp]
                teamed_students.update(team)
                students.difference_update(team)
                break
            else:
                team.add(wish)

    # print(students, teamed_students)
    print(m - len(teamed_students))
