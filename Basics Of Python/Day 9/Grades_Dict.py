student_scores = {
    "Harry":89,
    "Aakash":92,
    "Bhavesh":86,
    "Bharat":65,
    "Sejal":77,
    "Mansi":85
}
student_grades = {}
for i in student_scores:
    scores = student_scores[i]
    if scores > 90 :
        student_grades[i] = "Outstanding" 
    elif scores > 80 :
        student_grades[i] = "Exeeds Expectation"
    elif scores > 70 :
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
print(student_grades)