class Student:
    # students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        average = sum(*self.grades.values())/len(*self.grades.values())
        return round(average, 2)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}\
            \nКурсы в процессе изучения: {''.join(self.courses_in_progress)}\nЗавершенные курсы: {''.join(self.finished_courses)}"
        return res

    def comparison_students(self):
        if self.average_score() > 8:
            return "Отличная успеваемость"
        if self.average_score() < 9:
            return "Хорошая успеваемость"
        if self.average_score() < 7:
            return "Средняя успеваемость"
        if self.average_score() < 4:
            return "Плохая успеваемость"
        if self.average_score() < 2:
            return "Отчислить"
        else:
            return "Ошибка"

    # def add_student(self):
        # super().__init__()
        # Student.students_list.append(self)

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def average_score(self):
        average = sum(*self.grades.values())/len(*self.grades.values())
        return round(average, 2)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}"
        return res

    def comparison_lecturers(self):
        if self.average_score() > 8:
            return "Отличный результат"
        if self.average_score() < 9:
            return "Хороший результат"
        if self.average_score() < 7:
            return "Средний результат"
        if self.average_score() < 4:
            return "Плохой результат"
        if self.average_score() < 2:
            return "Уволить :)"
        else:
            return "Ошибка"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'PHP']
student1.finished_courses += ['JAVA']

student2 = Student('Nick', 'White', 'male')
student2.courses_in_progress += ['Python', 'C#']

student3 = Student('Susan', 'Mcdonald', 'female')
student3.courses_in_progress += ['Python', 'C++']

main_reviewer = Reviewer('George', 'Simons')
main_reviewer.courses_attached += ['Python']

lecturer1 = Lecturer('Mike', 'Rashford')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Robert', 'Rodgers')
lecturer2.courses_attached += ['Python']

lecturer3 = Lecturer('John', 'Dilan')
lecturer3.courses_attached += ['Python']


main_reviewer.rate_hw(student1, 'Python', 10)
main_reviewer.rate_hw(student1, 'Python', 8)
main_reviewer.rate_hw(student1, 'Python', 9)
main_reviewer.rate_hw(student2, 'Python', 6)
main_reviewer.rate_hw(student2, 'Python', 6)
main_reviewer.rate_hw(student2, 'Python', 6)
main_reviewer.rate_hw(student3, 'Python', 5)
main_reviewer.rate_hw(student3, 'Python', 10)
main_reviewer.rate_hw(student3, 'Python', 5)

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 9)
student3.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 5)
student3.rate_lecturer(lecturer2, 'Python', 7)
student1.rate_lecturer(lecturer3, 'Python', 8)
student2.rate_lecturer(lecturer3, 'Python', 5)
student3.rate_lecturer(lecturer3, 'Python', 7)

print(student1.grades)
print(lecturer1.grades)

print(main_reviewer)
print()
print(lecturer1)
print()
print(student1)

print(student1.comparison_students())
print(lecturer1.comparison_lecturers())


# student1.add_student
# student2.add_student
# student3.add_student

# print(Student.students_list)

# Не понял как выполнить 4 задание:
# 1) как добавить экземпляр класса в список?
# 2) если даже я добавлю экземпляр класса в список, то зачем нам три параметра(имя, фамилия, пол).
# 3) также нам нужно еще добавить только нужных студентов по определенному курсу..
# Я что-то совсем запутался в этом задании... 
