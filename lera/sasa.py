student_str = input(
    'Enter information about student with doubt\n'
    'Name,lastname,city,college,grades: '
)

student_info = student_str.split()
student = dict()
student['Name'] = student_info[0]
student['Lastname'] = student_info[1]
student['City'] = student_info[2]
student['College'] = student_info[3]
student['Grades'] = []
for i_grade in student_info[4:]:
    student['Grades'].append(int(i_grade))

for i_info in student:
    print(i_info,'-',student[i_info])