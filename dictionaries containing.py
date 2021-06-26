students = dict()
list1 = []
n = int(input("How many students are there: "))
for i in range(n):
    sname = input("Enter name of the student: ")
    marks = []

    for j in range(5):
        mark = float(input("Enter marks: "))
        marks.append(mark)
    students = {'name':sname,"marks" :marks}
    list1.append(students)


print("Create a dictionary students is ",list1)
"""
name = input ("Enter name of the student ")
if name in students.keys():
    print(students[name])
else:
    print("No student found this name")

    """