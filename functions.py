import json

class Student:
    def __init__(self,st_name,st_id = None,st_gr = "no group yet",st_book="no book yet",st_mark=None):
        self.student_id = st_id
        self.student_name = st_name
        self.student_group = st_gr
        self.student_book = st_book
        self.student_mark = st_mark

class Subject:
    def __init__(self,su_name,su_id = None,su_hours=None,id_students=[]):
        self.subject_name = su_name
        self.subject_id = su_id
        self.subject_hours = su_hours
        self.subject_students = []
        if(len(id_students) > 0):
            with open("db.json", "r") as data:
                dataloaded = json.loads(data.read())
                data.close()
            for i in range(len(id_students)):
                current_student_id = dataloaded['Students'][id_students[i] - 1]["ID"]
                current_student_name = dataloaded['Students'][id_students[i] - 1]["Name"]
                current_student_group = dataloaded['Students'][id_students[i] - 1]["Group"]
                current_student_book = dataloaded['Students'][id_students[i] - 1]["Book"]
                current_student_mark = dataloaded['Students'][id_students[i] - 1]["Mark"]
                created_student = Student(current_student_name,current_student_id,current_student_group,current_student_book,current_student_mark)
                self.subject_students.append(created_student)

class Teacher:
    def __init__(self,t_name,t_id=None,t_rank="Junior Teacher",t_hours=0,id_subjects = []):
        self.teacher_id = None
        self.teacher_name = t_name
        self.teacher_rank = t_rank
        self.teacher_hours = t_hours
        self.teacher_subjects = []
        if(len(id_subjects) > 0):
            with open("db.json", "r") as data:
                dataloaded = json.loads(data.read())
                data.close()
            for i in range(len(id_subjects)):
                current_subject_id = dataloaded['Subjects'][id_subjects[i] - 1]["ID"]
                current_subject_name = dataloaded['Subjects'][id_subjects[i] - 1]["Name"]
                current_subject_hours = dataloaded['Subjects'][id_subjects[i] - 1]["Hours"]
                current_subject_students = dataloaded['Subjects'][id_subjects[i] - 1]["Students"]
                created_subject = Subject(current_subject_name,current_subject_id,current_subject_hours,current_subject_students)
                self.teacher_subjects.append(created_subject)
                self.teacher_hours += current_subject_hours

#-------------Меню преподавателей----------------#
def teacher_menu():
    print("1 - Добавить нового преподавателя")
    print("2 - Отобразить преподавателей")
    print("3 - Редактирование преподавателя")
    choise = input("Ваш выбор: ")

    if(choise == "1"):
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            last_teacher = len(dataloaded["Teachers"]) - 1 #Ищем последнюю запись в БД
            name = input("Введите имя преподавателя: ")
            new_teacher = Teacher(name)
            if(last_teacher <= 0):
                information = {
                    "ID":1, #Здесь присваиваем ID при пустой базе данных
                    "Name":new_teacher.teacher_name,
                    "Rank":new_teacher.teacher_rank,
                    "Hours":new_teacher.teacher_hours,
                    "Subjects": new_teacher.teacher_subjects,
                }
            else:
                information = {
                    "ID":dataloaded["Teachers"][last_teacher]["ID"] + 1, #Здесь присваиваем ID больше последней записи
                    "Name":new_teacher.teacher_name,
                    "Rank":new_teacher.teacher_rank,
                    "Teacher Hours":new_teacher.teacher_hours,
                    "Subjects": new_teacher.teacher_subjects,
                }
            dataloaded["Teachers"].append(information)
            data.close()
        with open('db.json', 'w') as new_data:
            json.dump(dataloaded, new_data)
            new_data.close()

    if(choise == "2"):
        with open("db.json", "r") as data:
            print(json.dumps(json.load(data)["Teachers"], sort_keys=False, indent=4))
            data.close()

    if(choise == "3"):
        choise = input("Введите ID преподавателя: ")
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            data.close()
            teacher = dataloaded["Teachers"][int(choise)-1]
        print(teacher)
        print("Что редактируем?")
        print("1 - Имя")
        print("2 - Должность")
        print("3 - Добавляем предметы")
        choise = input("Ваш выбор: ")
        if(choise == "1"):
            new_name = input("Введите новое имя преподавателя: ")
            teacher["Name"] = new_name
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "2"):
            new_rank = input("Введите новую должность преподавателя: ")
            teacher["Rank"] = new_rank
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "3"):
            n = input("Введите ID предмета: ")
            with open("db.json", "r") as db:
                loaded_subjects = json.loads(db.read())
                db.close()
            subject = loaded_subjects["Subjects"][int(n)-1]
            teacher["Subjects"].append(subject["ID"])
            teacher["Teacher Hours"] += subject["Hours"]
            with open('db.json', 'w') as new_data:
                json.dump(dataloaded, new_data)
                new_data.close()

#-------------Меню предметов---------------------#
def subject_menu():
    print("1 - Добавить новый предмет")
    print("2 - Отобразить предметы")
    print("3 - Редактирование предметов")
    choise = input("Ваш выбор: ")

    if(choise == "1"):
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            last_subject = len(dataloaded["Subjects"]) - 1 #Ищем последнюю запись в БД
            name = input("Введите название предмета: ")
            hours = input("Введите количество часов предмета: ")
            new_subject = Subject(name,int(hours))
            if(last_subject <= 0):
                information = {
                    "ID":1, #Здесь присваиваем ID больше последней записи
                    "Name":new_subject.subject_name,
                    "Hours":new_subject.subject_hours,
                    "Students": new_subject.subject_students,
                    }
            else:
                information = {
                    "ID":dataloaded["Subjects"][last_subject]["ID"] + 1, #Здесь присваиваем ID больше последней записи
                    "Name":new_subject.subject_name,
                    "Hours":new_subject.subject_hours,
                    "Students": new_subject.subject_students,
                }
            dataloaded["Subjects"].append(information)
            data.close()
        with open('db.json', 'w') as new_data:
            json.dump(dataloaded, new_data)
            new_data.close()

    if(choise == "2"):
        with open("db.json", "r") as data:
            print(json.dumps(json.load(data)["Subjects"], sort_keys=False, indent=4))
            data.close()

    if(choise == "3"):
        choise = input("Введите ID предмета: ")
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            data.close()
        subject = dataloaded["Subjects"][int(choise)-1]
        print(subject)
        print("Что редактируем?")
        print("1 - Название")
        print("2 - Кол-во часов")
        print("3 - Добавляем студентов")
        choise = input("Ваш выбор: ")
        if(choise == "1"):
            new_name = input("Введите новое название предмета: ")
            subject["Name"] = new_name
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "2"):
            new_hours = input("Введите кол-во часов предмета: ")
            subject["Hours"] = new_hours
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "3"):
            n = input("Введите ID студента: ")
            with open("db.json", "r") as db_students:
                loaded_students = json.loads(db_students.read())
                db_students.close()
            student = loaded_students["Students"][int(n)-1]
            subject["Students"].append(student["ID"])
            with open('db.json', 'w') as new_data:
                json.dump(dataloaded, new_data)
                new_data.close()

#-------------Меню студентов---------------------#
def student_menu():
    print("1 - Добавить нового студента")
    print("2 - Отобразить студентов")
    print("3 - Редактирование студента")
    choise = input("Ваш выбор: ")

    if(choise == "1"):
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            last_student = len(dataloaded["Students"]) - 1 #Ищем последнюю запись в БД
            name = input("Введите имя студента: ")
            new_student = Student(name)
            if(last_student <= 0):
                information = {
                    "ID":1, #Здесь присваиваем ID больше последней записи
                    "Name":new_student.student_name,
                    "Group":new_student.student_group,
                    "Book Number":new_student.student_book_number,
                    "Mark":new_student.student_mark,
                }
            else:
                information = {
                    "ID":dataloaded["Students"][last_student]["ID"] + 1, #Здесь присваиваем ID больше последней записи
                    "Name":new_student.student_name,
                    "Group":new_student.student_group,
                    "Book Number":new_student.student_book_number,
                    "Mark":new_student.student_mark,
                }
            dataloaded["Students"].append(information)
            data.close()
        with open('db.json', 'w') as new_data:
            json.dump(dataloaded, new_data)
            new_data.close()

    if(choise == "2"):
        with open("db.json", "r") as data:
            print(json.dumps(json.load(data)["Students"], sort_keys=False, indent=4))
            data.close()

    if(choise == "3"):
        choise = input("Введите ID студента: ")
        with open("db.json", "r") as data:
            dataloaded = json.loads(data.read())
            data.close()
        student = dataloaded["Students"][int(choise)-1]
        print(student)
        print("Что редактируем?")
        print("1 - Имя студента")
        print("2 - Группу студента")
        print("3 - Номер зачётной книжки")
        choise = input("Ваш выбор: ")
        if(choise == "1"):
            new_name = input("Введите новое имя студента: ")
            student["Name"] = new_name
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "2"):
            new_group = input("Введите группу студента: ")
            student["Group"] = new_group
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
        if(choise == "3"):
            new_book = input("Введите номер зачётной книжки: ")
            student["Book Number"] = new_book
            with open('db.json', 'w') as data:
                json.dump(dataloaded, data)
                data.close()
