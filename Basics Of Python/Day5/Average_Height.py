student_heights = input("Enter Heights of Students : ").split()
n = 0
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum = 0
for i in student_heights:
    sum += i
average = sum//len(student_heights) 
print(f"Average height is {average}")