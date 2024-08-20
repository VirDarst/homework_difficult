grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Hendrik','Aaron'}
sorted_students=sorted(students)
average_grades={}
for index, student in enumerate(sorted_students):
    average = sum(grades[index]) / len(grades[index])
    average_grades[student] = average
print(average_grades)