# Imagine you're a teacher who needs to send a message to each of your students reminding them
# of their missing assignments and grade in the class.
# You have each of their names, number of missing assignments, and grades on a spreadsheet


names = list(input('Name'))
assignments = list(input('Missed assignments'))
grades = list(input('grade'))

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name in names:
    for assignment in assignments:
        for grade in grades:
            new_grade = grade + (assignment * 2)
            print(message.format(name, assignment, grade, new_grade))


###

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))