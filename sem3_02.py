# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
lst = [2, 3, 5, 6]
new_lst= []
length = 0
if len(lst) % 2 != 0:
    length = len(lst) // 2 + 1
else:
    length = len(lst) // 2

for i  in range(length):
    new_lst.append(lst[i] * lst[len(lst) - i - 1])
print(new_lst)