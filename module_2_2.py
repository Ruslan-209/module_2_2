# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0


numbers1 = str(input('введите первое число: '))
numbers2 = str(input('введите второе число: '))
numbers3 = str(input('введите третье число: '))
print(numbers1, numbers2, numbers3)

if numbers1 == numbers2 == numbers3:
    print('third')
elif numbers1 == numbers2 or numbers1 == numbers3 or numbers2 == numbers3:
    print('second')
else:
    print('first')
