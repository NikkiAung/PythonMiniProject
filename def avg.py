def marks(a):
    total = 0
    count = 0
    for i in range(0,len(a)):
        total += a[i]
        count += 1
    avg = total/count
    print(avg)
    if avg >= 80:
        print('Grade A')
    elif avg >= 60 or avg < 80:
        print('Grade B')
    elif avg >= 50 or avg < 60:
        print('Grade C')
    elif avg < 50:
        print('Grade F')

marks([55,64,75,80,65])


or

def averageMark(marks):
    sum_of_mark = sum(marks)
    total_subject = len(marks)
    avg = sum_of_mark / total_subject
    return avg



marks = [55,64,75,80,65]
average_mark = averageMark(marks)
print(average_mark)

def grading(average_mark):
    if average_mark >= 80:
        return 'Grade A'
    elif average_mark >= 60 or avg < 80:
        return 'Grade B'
    elif average_mark >= 50 or avg < 60:
        return 'Grade C'
    elif average_mark < 50:
        return 'Grade F'

grading_level = grading(average_mark)
print(grading_level)