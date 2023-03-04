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
        
    # Создаю статический метод для подсчета среднего арифметического оценок
    @staticmethod
    def __get_average(grades):
        # Если оценки сущестуют
        if grades:
            # Сумма оценок
            s = 0
            # Количество оценок
            l = 0
            for grade in grades.values():
                s += sum(grade)
                l += len(grade)
            #Возвращаю сумму/кол-во 
            return round(s/l,1)
        # Если оценок нет - возвращаю ноль
        else:
            return 0
        
    # Перегружаю __str__
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.__get_average(self.grades)} \
            \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \
            \nЗавершенные курсы: {', '.join(self.finished_courses)}"
    
    # Перегражаю __lt__ (< сравнение)
    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не студент!')
            return  
        if self.__get_average(self.grades) < other.__get_average(other.grades):
            return f'У {self.name} оценки хуже {other.name}'
        else:
            return f'У {self.name} оценки лучше {other.name}'
    

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'
        

class Lecturer(Mentor):

    def __init__(self, name, surname):
        # Инициализирую от родителя
        super().__init__(name,surname)
        # Инициализирую оценки лектора
        self.grades = {}

    # Перегружаю __str__
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредння оценка за лекции: {self.__get_average(self.grades)}'
    
    # Создаю статический метод для подсчета среднего арифметического оценок
    @staticmethod
    def __get_average(grades):
        # Если оценки сущестуют
        if grades:
            # Сумма оценок
            s = 0
            # Количество оценок
            l = 0
            for grade in grades.values():
                s += sum(grade)
                l += len(grade)
            #Возвращаю сумму/кол-во 
            return round(s/l,1)
        # Если оценок нет - возвращаю ноль
        else:
            return 0
        
    # Перегражаю __lt__ (< сравнение)
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не лектор!')
            return  
        if self.__get_average(self.grades) < other.__get_average(other.grades):
            return f'У лектора {self.name} оценки хуже {other.name}'
        else:
            return f'У лектора {self.name} оценки лучше {other.name}'

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    # Перегружаю __str__    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def get_ave(objs,course_name):
    average = 0
    for obj in objs:
        if course_name in obj.grades:
            s = 0
            l = 0
            for grade in obj.grades[course_name]:
                s += grade
                l += 1
            average += round(s/l,1)
        else: 
            return 0
    return round(average/len(objs),1)

# Функция получения всех entity (объектов) нужного класса посредством globals()
def get_all_entity(class_name):
    gl = globals().copy()
    all_entity = []
    for i in gl.values():
        if isinstance(i, class_name):
            all_entity.append(i)
    return all_entity

#Тест
# Задание 4
# Создаю объекты студента 1 и студента 2
student1 = Student('Кирилл','Полетаев','Мужчина')
student2 = Student('Иван','Ракитин','Мужчина')
# Создаю объекты лектора 1 и лектора 2
lecturer1 = Lecturer('Игорь', 'Алексеев')
lecturer2 = Lecturer('Дмитрий', 'Бочаров')
# Создаю объект ревьювера 1
reviewer1 = Reviewer('Егор','Налимов')
reviewer2 = Reviewer('Дарья','Котова')
# Создаю обхекты ментора 1 и ментора 2
mentor1 = Mentor('Алиса','Мышкина')
mentor2 = Mentor('Григорий','Горин')
# Добавляю студентов на курсы
courses1 = ['Python', 'Csharp','HTML CSS JS']
courses2 = ['English', 'Deutsch']
student1.courses_in_progress = courses1
student1.finished_courses = courses2
student2.courses_in_progress = courses1
student2.finished_courses = courses2

# Добавляю лекторов и ревьюверов на курсы
lecturer1.courses_attached = courses1.copy()
lecturer1.courses_attached += courses2.copy()
lecturer2.courses_attached = courses1.copy()
lecturer2.courses_attached += courses2.copy()
reviewer1.courses_attached = courses1.copy()
reviewer2.courses_attached = courses2.copy()
# Выставляю оценки студентам ревьюверами
reviewer1.rate_hw(student1,'Python',8)
reviewer1.rate_hw(student1,'Csharp',7)
reviewer1.rate_hw(student1,'Python',10)
reviewer1.rate_hw(student1,'HTML CSS JS',3)
reviewer1.rate_hw(student2,'Python',3)
reviewer1.rate_hw(student2,'HTML CSS JS',6)

reviewer2.rate_hw(student1,'English',1)
reviewer2.rate_hw(student1,'Deutsch',1)
reviewer1.rate_hw(student1,'Csharp',2)
reviewer1.rate_hw(student2,'Csharp',5)

# Выставляю оценки лекторам студентами
student1.rate_lecturer(lecturer1,'Python', 10)
student1.rate_lecturer(lecturer2,'Python', 7)
student1.rate_lecturer(lecturer1,'Csharp', 3)
student1.rate_lecturer(lecturer1,'HTML CSS JS', 7)
student1.rate_lecturer(lecturer2,'English', 8)
student1.rate_lecturer(lecturer2,'Deutsch', 10)

student2.rate_lecturer(lecturer1,'Python', 6)
student2.rate_lecturer(lecturer2,'Python', 5)
student2.rate_lecturer(lecturer1,'Csharp', 2)
student2.rate_lecturer(lecturer1,'HTML CSS JS', 1)
student2.rate_lecturer(lecturer2,'English', 7)
student2.rate_lecturer(lecturer2,'Deutsch', 3)

print('---Студент 1---')
print(student1)
print('---Студент 2---')
print(student2)
print('---Лектор 1---')
print(lecturer1)
print('---Лектор 2---')
print(lecturer2)
print('---Ревьювер 1---')
print(reviewer1)
print('---Ревьювер 2---')
print(reviewer2)
print('---Сравнение оценок студентов---')
print(student1 < student2)
print('---Сравнение оценок лекторов---')
print(lecturer1 < lecturer2)

# Тест с выставленным большим кол-вом оценок у студентов и лекторов
# student1.grades['Python'] += [9,8,3,5,7,8,3,9,9,9,9]
# student2.grades['Python'] += [2,5,6,8,4,5,3]
# lecturer1.grades['Python'] += [2,8,3,3,3,3,3]
# lecturer2.grades['Python'] += [8,8,3,8,4,8,9,0,0]


# Получить среднюю оценку за домашние задания по всем студентам в рамках конкретного курса
print('---Средняя оценка студентов на курсе Python---')
print(f"Средняя оценка по всем студентам на курсе Python: {get_ave(get_all_entity(Student), 'Python')}")

# Получить среднюю оценки за лекции всех лекторов в рамках курса
print('---Средняя оценка лекторов на курсе Python---')
print(f"Средняя оценка по всем лекторам на курсе Python: {get_ave(get_all_entity(Lecturer), 'Python')}")