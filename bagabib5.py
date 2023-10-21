from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
   Student('Махир', '34', 4.7, 'Баклань'),
   Student('Александр', '17', 4.3, 'Новосибирск'),
   Student('Владимир', '22', 5, 'Рожки'),
   Student('Мафусаил', '24', 4.6, 'Такое'),
   Student('Николай', '19', 3.2, 'Санкт-Петербург'),
   Student('Владислав', '20', 3.9, 'Хабаровск'),
   Student('Генадий', '29', 4.8, 'Дешевки')
)
def j(students):
   z = 0

   for student in students:
       z += student.grade
   ussr = z / len(students)

   f = [student.name for student in students if student.grade >= ussr]
   print('Ученики ', ', '.join(f), ' в этом семестре хорошо учатся!')

j(students)