from urllib.response import addbase

my_dict = {'Igor' : 1994, 'Vladimir' : 1952, 'Don' : 1976}
print(my_dict['Igor'])
my_dict.update({'Sasha' : 2000, 'Anna' : 2007})
print(my_dict)
del my_dict['Don']
print(my_dict.get('Don', 'Значение удалено!')) # Значение удалено из словоря

#Удалите одну из пар в словаре для существующего ключа из словаря my_dict и введите значение из этой пары на экране.
# Не понимаю, что конкретно требуется. Надеюсь решено верно))))

my_set = {1,2,3,4,2,2,2,3,4,1,2, True, 'Строка', (1,2,3,3,2,1),'Строка'}
print(my_set)
my_set.add('Слово')
my_set.add((7,8,8))
my_set.discard((1,2,3,3,2,1))
print(my_set)