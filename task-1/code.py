
# University Scholarship Allocation System

students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))
    maths = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (aggregate >= 75 and maths >= 60 and
        physics >= 60 and chemistry >= 60 and
        attendance >= 75 and income <= 250000):

        print(name, "is Eligible for Scholarship")

        eligible.append([name, aggregate, attendance, income])

    else:
        print(name, "is Not Eligible")

# Ranking eligible students
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n----- SCHOLARSHIP RANK LIST -----")

if len(eligible) == 0:
    print("No students are eligible for scholarship")

else:
    rank = 1

    for student in eligible:
        print("\nRank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])

        rank += 1

print("\nTotal Eligible Students:", len(eligible))

