
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)                        #Перевожу множество в список.
students.sort()                                  #Сортирую список в алфавитном порядке.

sr_znach_1 = sum(grades[0]) / len(grades[0])     #Извлекаю группы элементов по индексу и нахожу для каждого среднее арифметическое значение.
sr_znach_2 = sum(grades[1]) / len(grades[1])
sr_znach_3 = sum(grades[2]) / len(grades[2])
sr_znach_4 = sum(grades[3]) / len(grades[3])
sr_znach_5 = sum(grades[4]) / len(grades[4])

grades_sred = [sr_znach_1,sr_znach_2,sr_znach_3,sr_znach_4,sr_znach_5]     #Создаю список из значений

average_rating = dict(zip(students,grades_sred))                           #Создаю словарь, объединяя два списка
print(average_rating)