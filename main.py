from functions import *

print("1 - Управление преподавателями")
print("2 - Управление предметами")
print("3 - Управление студентами")
choise = input("Ваш выбор: ")
if(choise == "1"):
    teacher_menu()
if(choise == "2"):
    subject_menu()
if(choise == "3"):
    student_menu()
'''
white = Teacher("Mr.White")
brown = Teacher("Mr.Brown")

first = Student("Adam First")
second = Student("Larry Second")

math = Subject("Math", 24)
physics = Subject("Physics", 20)
chemistry = Subject("Chemistry", 16)

#white.add_subject(math)
#white.add_subject(physics)

math.set_subject_teacher(white)
physics.set_subject_teacher(brown)
chemistry.set_subject_teacher(brown)

first.add_student_to_subject(math)
first.add_student_to_subject(physics)
second.add_student_to_subject(math)

#show_subjects()
#showdb()
'''
