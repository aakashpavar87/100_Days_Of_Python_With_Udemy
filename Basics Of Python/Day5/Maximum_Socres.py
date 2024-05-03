student_marks = input("Enter Marks of The Students : ").split()
for i in range(0, len(student_marks)):
    student_marks[i] = int(student_marks[i])

max = 0
for i in student_marks:
    if(i > max):
        max = i
print(f"Maximum out of List Is : {max}")