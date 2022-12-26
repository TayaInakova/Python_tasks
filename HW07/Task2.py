# 2) Нужно написать программу. В ней используем классы -
# имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени,
# А так же студентов, у которых низкие оценки
from random import randint


# встроенные методы определяют курс студента по его возрасту и генерирует рандомный список оценок,
# по которому вычисляется средний балл


class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name}'

    def group(self):
        if 16 < self.age < 19:
            return 1
        elif 18 < self.age < 21:
            return 2
        elif 20 < self.age < 23:
            return 3
        elif 22 < self.age < 25:
            return 4

    def progress(self):
        progress_list = []
        for _ in range(7):
            progress_list.append(randint(2, 5))
        average_score = round(
            ((5 * progress_list.count(5)) + (4 * progress_list.count(4)) + (3 * progress_list.count(3)) + (
                    2 * progress_list.count(2))) / (
                    progress_list.count(5) + progress_list.count(4) + progress_list.count(3) + progress_list.count(
                2)))
        return average_score


auditorium = []

for i in range(10):
    student_name = ['Маша', 'Геннадий', 'Роман', 'Ольга',
                    'Ирина', 'Степан', 'Николай', 'Варвара', 'Иван', 'Сергей']
    y = Student(student_name[i], randint(17, 24))
    a = [y, y.name, y.age, y.group(), y.progress()]
    auditorium.append(a)

auditorium = sorted(auditorium, key=lambda x: x[1])

for q in range(len(auditorium)):
    print(
        f'Имя: {auditorium[q][1]}, \nВозраст: {auditorium[q][2]}, \nКурс: {auditorium[q][3]}\nСредний балл: {auditorium[q][4]}\n')

academic_failure = list(filter(lambda x: x[4] < 4, auditorium))

print('Список неуспевающих:\n')
for q in range(len(academic_failure)):
    print(
        f'Имя: {academic_failure[q][1]}, \nВозраст: {academic_failure[q][2]}, \nКурс: {academic_failure[q][3]}\nСредний балл: {academic_failure[q][4]}\n')
