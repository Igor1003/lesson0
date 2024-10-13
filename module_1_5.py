immutable_var = 1, 2, 3, True, 'Hallo'
print(immutable_var)
#immutable_var[0] = 5 # Ошибка типа: объект «кортеж» не поддерживает назначение элементов



mutable_list = ['A', 'b', 1, 2, 'dog']
mutable_list[0] = 'C'
mutable_list[1] = 'd'
mutable_list[2] = 5
mutable_list[4] = 'cat'
print(mutable_list)