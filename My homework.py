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
        res = [j for i in [self.grades.values()] for j in i]
        a = [j for i in res for j in i]
        average = sum(map(sum, self.grades.values()))/len(a)
        return round(average, 2)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}\
            \nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Студент не найден")
            return
        return self.average_score() < other.average_score()

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
        res = [j for i in [self.grades.values()] for j in i]
        a = [j for i in res for j in i]
        average = sum(map(sum, self.grades.values()))/len(a)
        return round(average, 2)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Лектор не найден")
            return
        return self.average_score() < other.average_score()

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
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['PHP']
student1.finished_courses += ['JAVA']

student2 = Student('Nick', 'White', 'male')
student2.courses_in_progress += ['Python', 'C#']

student3 = Student('Susan', 'Mcdonald', 'female')
student3.courses_in_progress += ['Python', 'C++']

main_reviewer = Reviewer('George', 'Simons')
main_reviewer.courses_attached += ['Python']
main_reviewer.courses_attached += ['PHP']

lecturer1 = Lecturer('Mike', 'Rashford')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['PHP']

lecturer2 = Lecturer('Robert', 'Rodgers')
lecturer2.courses_attached += ['Python']

lecturer3 = Lecturer('John', 'Dilan')
lecturer3.courses_attached += ['Python']


main_reviewer.rate_hw(student1, 'Python', 10)
main_reviewer.rate_hw(student1, 'Python', 8)
main_reviewer.rate_hw(student1, 'Python', 9)
main_reviewer.rate_hw(student1, 'PHP', 7)
main_reviewer.rate_hw(student1, 'PHP', 8)
main_reviewer.rate_hw(student1, 'PHP', 8)
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
student3.rate_lecturer(lecturer3, 'Python', 6)

print(student1.grades)
print(lecturer1.grades)

print(main_reviewer)
print()
print(lecturer3)
print()
print(student1)

print(student1 > student2)
print(lecturer1 < lecturer2)

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# list_of_students = []

# list_of_students.append(student1)
# list_of_students.append(student2)
# list_of_students.append(student3)

# # for student, grades in student1.items():
# #     for grade in grades:
# #         print(grade)

