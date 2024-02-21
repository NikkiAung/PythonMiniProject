StudentName = ['Aung', 'David', 'Crown', 'Kelvin', 'Emily']
StudentMark = [[100,96,90,100,86],
               [67,56,54,54,23],
               [56,23,45,12,14],
               [56,12,3,35,13],
               [10,100,24,45,90]]
ClassSize = 5
SubjectNo = 5
average_mark_with_name = []
for i in range(0,len(StudentName)):
    x = StudentMark[i]
    res1 = StudentName[i], 'total mark is', x[0] + x[1] + x[2] + x[3] + x[4]
    res2 = StudentName[i], 'average mark is', (x[0] + x[1] + x[2] + x[3] + x[4]) // 5
    avg = StudentName[i], (x[0] + x[1] + x[2] + x[3] + x[4]) // 5
    print('-' * 23)
    print(res1)
    print(res2)
    average_mark_with_name.append(avg)
print('=' * 40)
print(average_mark_with_name)

count_for_distinction = 0
count_for_merit = 0
count_for_normal = 0
count_for_fail = 0
for u in range(0,len(average_mark_with_name)):
    if average_mark_with_name[u][1] >= 70:
        print(average_mark_with_name[u][0], 'passed with distinction')
        count_for_distinction += 1
    elif average_mark_with_name[u][1] >= 55 and average_mark_with_name[u][1] < 70:
        print(average_mark_with_name[u][0], 'passed with merit')
        count_for_merit += 1
    elif average_mark_with_name[u][1] >= 40 and average_mark_with_name[u][1] < 55:
        print(average_mark_with_name[u][0], 'passed with normal')
        count_for_normal += 1
    elif average_mark_with_name[u][1] < 40:
        print(average_mark_with_name[u][0], 'fail')
        count_for_fail += 1
print('-'*55)
print('count_for_distinction',count_for_distinction)
print('count_for_merit ', count_for_merit )
print('count_for_normal',count_for_normal)
print('count_for_fail',count_for_fail)