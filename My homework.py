class Student:
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
        return average

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
        return average

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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'PHP']
best_student.finished_courses += ['JAVA']

another_student = Student('Nick', 'White', 'male')
another_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

great_lecturer = Lecturer('Mike', 'Rashford')
great_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
best_student.rate_lecturer(great_lecturer, 'Python', 10)
another_student.rate_lecturer(great_lecturer, 'Python', 5)

print(best_student.grades)
print(great_lecturer.grades)

print(cool_reviewer)
print()
print(great_lecturer)
print()
print(best_student)

print(best_student.comparison_students())
print(great_lecturer.comparison_lecturers())