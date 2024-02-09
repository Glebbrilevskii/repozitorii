# в питоне есть 2 вида циклов - for(для), while(пока)
# циклы мы можем использовать только с итерируемыми объектами (массивы)
# names = ["gleb", "kiril", "stas"]
# for name in names:
#     print(name)
# итерация - один прокрут цикла
# range(старт, стоп, степ)
# a = range(100)
# print(a)
# print(list(a))

# for number in range(10):
#     print(number)

# функция enumerate(iterable)
# a = [1,2,3]
# for index, value in enumerate(a):
#     print(index, value)
# возвращает список кортежей которые состоят из 2 элементов (индекс, значение) на примере выше
# со списком получаем [(0,1), (1,2), (2,3)]
# a = [("gleb", "brilevskii", 23), ("stas", "wanrl", 14), ("inna", "trav", 26)]
# for name, surname, age in a:
#     print(name, surname, age)

# операторы break, continue
# оператор break принудительно завершает цикл
# оператор continue на моменте объявления переходит в следующую итерацию
# a = [1,4,7,23,56]
# for i in a:
#     if i == 7:
#         continue
#     print(i)
# a = [1,4,7,23,56]
# for i in a:
#     if i % 2 == 0:
#         break
#     print(i)
#  у цикла for и цикла while есть else который сработает в том случае если все итерации цикла были пройдены
# a = [1,2,3,4,5]
# for i in a:
#     if i == 5:
#         break
#     print(i)
# else:
#     print("Цикл завершен успешно")

#  цикл while пока какое-то условие True будут работать итерации
# a = 1
# while a <= 10:
#     print(a)
#     a += 1   #a = a + 1

# a = {"apple": 10, "banana": 25, "orange": 15, "peach": 30}
# wallet = 50
# b = []
# for key, value in a.items():
#     if wallet - value >= 0:
#         wallet -= value
#         b.append(key)
# print(b)

# ДЗ
# программа загадывает число, пользователь вводит число пока не угадает, как только пользователь
# угадал число - программа завершается
# chislo = 5
# while True:
#     if int(input()) == chislo:
#         print("верно")
#         break
#     else:
#         print("не верно")

# есть черный и белый список, в них лежат числа. если число из черного списка есть в белом, тогда ничего не делаем,
# а выводим что "Числа плохие". Если же чисел из черного списка нет в белом, тогда выводим что "Все хорошо"
# black_list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# white_list = {21, 22, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# a = black_list.symmetric_difference(white_list)
# b = black_list.union(white_list)
# if a != b:
#     print("Числа плохие")
# else:
#     print("Все хорошо")

# white_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# black_list = [21, 1, 12, 13, 14, 15, 16, 17, 18,]
# for i in white_list:
#     if i in black_list:
#         print("Числа плохие")
#         break
# else:
#     print("Все хорошо")



# необходимо вывести на консоль последовательность чисел - 1 2 4 8 16 32 64 128 256 512, 1 число, 1 принт, без списков
# a = 1
# while a < 512:
#     a += a
#     print(a)

# дан список чисел любой длинны, нужно вывести True если 2 одинаковых числа стоят рядом друг с другом и False,
# если таких чисел нет
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# for index, value in enumerate(a):
#     if len(a) == index +1:
#         print(False)
#         break
#     if value == a[index +1]:
#         print(True )
#         break




