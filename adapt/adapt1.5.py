grade = str(input())
massive_grade = []
n = 0
len_grade = 0
for i in range(len(grade)):
    if grade[i] != ' ':
        massive_grade.append(grade[i])
        len_grade +=1
    if grade[i] == 'A':
        n += 1
persent = float(n/len_grade)
print('%.2f'%persent)
