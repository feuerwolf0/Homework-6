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

#Тест
# Создаю обьект класса Лектор
lector1 = Lecturer('Олег', 'Алексеев')
# Добавляю объекту лектора закрепленный за ним курс
lector1.courses_attached.append('Just course')
# Создаю обьект класса Студент
student1 = Student('Kirill','Poletaev','male')
# Добавляю студенту курс Just course в "курсы в процессе"
student1.courses_in_progress.append('Just course')
# Выставляю обектом студента оценку объекту лектора
student1.rate_lecturer(lector1,'Just course',9)
# Проверяю атрибуты объекта лектора
# print(lector1.__dict__)

print('-' * 5 +'Принт ревьювера' + '-' * 5)
# Создаю объект ревьювера
reviewer1 = Reviewer('Владислав', 'Попов')
# Печатаю объект ревьювера
print(reviewer1)

# Тест задание 3.

print('-' * 5 +'Принт Лектора 1' + '-' * 5)

# Добавляю объекту лектор 2 курса и оценки к нему
lector1.grades['First course'] = [3,8,7]
lector1.grades['Second course'] = [5,10,8]
# Печатаю объект лектора
print(lector1)

print('-' * 5 +'Принт студента 1' + '-' * 5)

# Добавляю обьекту студента завершенные курсы и оценки к ним
student1.finished_courses.append('First course')
student1.finished_courses.append('Second course')
student1.grades['First course'] = [5,7,9]
student1.grades['Second course'] = [10,10,3,1]
student1.grades['Just Course'] = [8]
# Печатаю объект студента
print(student1)

print('-' * 5 +'Принт Студента 2' + '-' * 5)
# Добавляю второго студента для сравнения
student2 = Student('Иван', 'Нечаев', 'male')
student2.finished_courses.append('First course')
student2.grades['First course'] = [1,10,8,7,6,4]
print(student2)
print('-' * 5 +'Сравнение оценок студентов' + '-' * 5)

# Сравниваю оценки двух студентов
print(f'{student1 > student2}')
print('-' * 5 +'Принт лектора 2' + '-' * 5)

# Добавляю второго лектора
lector2 = Lecturer('Евгений', 'Рясин')
lector2.courses_attached.append('Just course')
lector2.grades['First course'] = [3,2,3]
lector2.grades['Second course'] = [1,10,8,9]
print(lector2)

print('-' * 5 +'Сравнение оценок лекторов' + '-' * 5)
# Сравниваю двух лекторов
print(lector1 < lector2)