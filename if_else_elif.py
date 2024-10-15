first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)
    #Старайтесь избегать вложенности условий и описывать их, используя операторы or, and и not.
    #Если, что то сделал не так, то намекните как правильно. Я не совсем понимаю примечание, о не использовании or, and и not , если я их только изучил.