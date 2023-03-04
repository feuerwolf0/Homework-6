class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        # Проверка оценки от 0 до 10 (по 10-и бальной шкале)
        if 0 <= grade <= 10:
            # Проверка Если лектор объект класса Лектор, студент окончил курс или курс в процессе, лектор ведет этот курс
            if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Ошибка')
                return 'Ошибка'
        else:
            print('Ошибка, введите оценку от 0 до 10') 
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Инициализирую от родителя
        super().__init__(name,surname)
        # Инициализирую оценки лектора
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#Тест
# Создаю обьект класса Лектор
lector1 = Lecturer('Name', 'Fam')
# Добавляю объекту лектора закрепленный за ним курс
lector1.courses_attached.append('Just course')
# Создаю обьект класса Студент
student1 = Student('Kirill','Poletaev','male')
# Добавляю студенту курс Just course в "курсы в процессе"
student1.courses_in_progress.append('Just course')
# Выставляю обектом студента оценку объекту лектора
student1.rate_lecturer(lector1,'Just course',9)
# Проверяю атрибуты объекта лектора
print(lector1.__dict__)