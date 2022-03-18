from studygroup import *

student1 = Student('Иван', 'Иванов', 'М')
student2 = Student('Петр', 'Петров', 'М')

student1.finished_courses += ['Системы отопления', 'GIT']
student1.courses_in_progress += ['Python', 'Java', 'C++', 'C#', 'Менеджмент', 'Маркетинг']
student2.finished_courses += ['Системы отопления', 'GIT']
student2.courses_in_progress += ['Python', 'Java', 'C++', 'Менеджмент', 'Маркетинг']

reviewer1 = Reviewer('Мумий', 'Тролль')
reviewer1.courses_attached += ['Python', 'Java', 'C++', 'C#']
reviewer2 = Reviewer('Аркадий', 'Укупник')
reviewer2.courses_attached += ['Менеджмент', 'Маркетинг', 'Системы отопления']

lecturer1 = Lecturer('Филипп', 'Киркоров')
lecturer1.courses_attached += ['Python', 'Java', 'C++', 'C#']
lecturer2 = Lecturer('Семен', 'Слепаков')
lecturer2.courses_attached += ['Python', 'Менеджмент', 'Маркетинг', 'Системы отопления']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Java', 8)
reviewer1.rate_hw(student1, 'Java', 9)
reviewer1.rate_hw(student1, 'Java', 6)
reviewer2.rate_hw(student1, 'Менеджмент', 9)
reviewer2.rate_hw(student1, 'Менеджмент', 5)
reviewer2.rate_hw(student1, 'Менеджмент', 2)
reviewer2.rate_hw(student1, 'Маркетинг', 6)
reviewer2.rate_hw(student1, 'Маркетинг', 4)
reviewer2.rate_hw(student1, 'Маркетинг', 10)

reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Java', 3)
reviewer1.rate_hw(student2, 'Java', 9)
reviewer1.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Менеджмент', 4)
reviewer2.rate_hw(student2, 'Менеджмент', 9)
reviewer2.rate_hw(student2, 'Менеджмент', 3)
reviewer2.rate_hw(student2, 'Маркетинг', 1)
reviewer2.rate_hw(student2, 'Маркетинг', 1)
reviewer2.rate_hw(student2, 'Маркетинг', 10)

student1.rate_lecturer(lecturer1, 'Python', 5)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Java', 4)
student1.rate_lecturer(lecturer1, 'Java', 2)
student1.rate_lecturer(lecturer1, 'Java', 10)
student2.rate_lecturer(lecturer1, 'Python', 2)
student2.rate_lecturer(lecturer1, 'Python', 3)
student2.rate_lecturer(lecturer1, 'Python', 6)
student2.rate_lecturer(lecturer1, 'Java', 7)
student2.rate_lecturer(lecturer1, 'Java', 9)
student2.rate_lecturer(lecturer1, 'Java', 4)

student1.rate_lecturer(lecturer2, 'Python', 8)
student1.rate_lecturer(lecturer2, 'Python', 7)
student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Маркетинг', 9)
student1.rate_lecturer(lecturer2, 'Маркетинг', 6)
student1.rate_lecturer(lecturer2, 'Маркетинг', 7)
student2.rate_lecturer(lecturer2, 'Python', 3)
student2.rate_lecturer(lecturer2, 'Python', 4)
student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Маркетинг', 7)
student2.rate_lecturer(lecturer2, 'Маркетинг', 5)
student2.rate_lecturer(lecturer2, 'Маркетинг', 4)

print('Студент 1')
print(student1)
print('Студент 2')
print(student2)

print('Ревьювер 1')
print(reviewer1, end='\n\n')
print('Ревьювер 2')
print(reviewer2, end='\n\n')

print('Лектор 1')
print(lecturer1)
print('Лектор 2')
print(lecturer2)

print(f'Студент 1 = Студент 2 : {student1 == student2}')
print(f'Студент 1 > Студент 2 : {student1 > student2}')
print(f'Студент 1 < Студент 2 : {student1 < student2}')
print()
print(f'Лектор 1 = Лектор 2 : {lecturer1 == lecturer2}')
print(f'Лектор 1 > Лектор 2 : {lecturer1 > lecturer2}')
print(f'Лектор 1 < Лектор 2 : {lecturer1 < lecturer2}')
print()
print(f'Средняя оценка за ДЗ по курсу Python: {course_avegrade_students([student1, student2], "Python")}')
print(f'Средняя оценка за лекции по курсу Python: {course_avegrade_lecturers([lecturer1, lecturer2], "Python")}')
