# Проверки в питоне нужны что бы узнать логически какой участок кода выполнять
# Это один блок проверки и выполнится одно действие, потому что у нас есть else
# a = 12
# if a % 2 == 0:
#     print("Четное число")
# elif a % 5 == 0:
#     print("Число делится на 5")
# else:
#     print("Нечетное число")
# if может быть один, без elif и else
# кол-во elif неограничено

# # Операторы and, or, not
# a = 1 and 2
# print(a)
# # and - оценивает второй аргумент, только если первый равен True. Если в цепочке and все операнды являются истиной,
# результатом будет последнее значение. А если какой-либо из операндов является False,
# результатом будет первое ложное значение

# b = 1 or 0
# print(b)
# # or - оценивает второй аргумент, только если первый равен False. Если какой-либо операнд в цепочке or
# является истиной, немедленно возвращается резулььтат - первое истиное значение

# # not возвращает противоположное логическое значение
# c = not False
# print(c)

# a = [5, 15, 20, 19]
# if a[0] % 5 == 0 and a[1] % 5 == 0 and a[2] % 5 == 0 and a[3] % 5 == 0:
#     print("Все числа деляться на 5")

# b = [100, 200, 300, 400, 500]
# c = (b[0] + b[1] + b[2] + b[3] + b[4]) / 5
# if c >= 200 and c <= 300:
#     print("Число в диапозоне")

# Операторы in
# a = 2 in [1,2,3]
# print(a)
#
# a = {"name":'Юля'}
# b = ["Глеб", "Кирил", "Юля"]
# c = ["Стас", "Тимур", "Настя"]
# if a["name"] in b:
#     print("Юля в команде Б")
# elif a["name"] in c:
#     print("Юля в команде С")
# else:
#     print("Юли нету нигде")

# if a["name"] in b or a["name"] in c:
#     print("Есть в команде")