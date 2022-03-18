class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if self.get_average_grade():
            text = (f'Имя: {self.name}\n'
                    f'Фамилия: {self.surname}\n'
                    f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
                    f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                    f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
            return text
        else:
            text = (f'Имя: {self.name}\n'
                    f'Фамилия: {self.surname}\n'
                    f'Средняя оценка за домашние задания: оценок пока нет.\n'
                    f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                    f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
            return text

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
            return 'Lecturer rated'
        else:
            return 'Error'

    def get_average_grade(self):
        sum_of_grades = 0
        number_of_grades = 0
        for course_grades in self.grades.values():
            sum_of_grades += sum(course_grades, 0)
            number_of_grades += len(course_grades)
            if number_of_grades > 0:
                average_grade = sum_of_grades / number_of_grades
                return average_grade
            else:
                return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        text = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
        return text


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
            return 'HW rated'
        else:
            return 'Error'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if self.get_average_grade():
            text = (f'{super().__str__()}\n'
                    f'Средняя оценка за лекции: {self.get_average_grade()}\n')
            return text
        else:
            text = (f'{super().__str__()}\n'
                    f'Средняя оценка за лекции: у лектора еще нет оценок.\n')
            return text

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        return

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return

    def get_average_grade(self):
        sum_of_grades = 0
        number_of_grades = 0
        for course_grades in self.grades.values():
            sum_of_grades += sum(course_grades, 0)
            number_of_grades += len(course_grades)
            if number_of_grades > 0:
                average_grade = sum_of_grades / number_of_grades
                return average_grade
            else:
                return 0


def course_avegrade_students(students, course):
    sum_of_grades = 0
    num_of_grades = 0
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            sum_of_grades += sum(student.grades[course], 0)
            num_of_grades += len(student.grades[course])
    if num_of_grades > 0:
        average_course_grade = sum_of_grades / num_of_grades
        return average_course_grade
    else:
        return 0


def course_avegrade_lecturers(lecturers, course):
    sum_of_grades = 0
    num_of_grades = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            sum_of_grades += sum(lecturer.grades[course], 0)
            num_of_grades += len(lecturer.grades[course])
    if num_of_grades > 0:
        average_course_grade = sum_of_grades / num_of_grades
        return average_course_grade
    else:
        return 0
