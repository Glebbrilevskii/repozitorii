# 1. если число палиндром (читается одинаково задом на перед 121, 202 и т.д.) вывести True, если нет False
# a = 101
# b = a % 10
# c = a // 100
# if b == c:
#     print("True")
# else:
#     print("False")

# def number(a):
#     :
#         print("True")
#     elif b != c:
#         print("False")
# g = number(a=101)


# 2. даны 2 списка, объедините два списка в один отсортированный список.
#отсортировать в функции
# list_1 = [1,2,4,6]
# list_2 = [3,7,8,5]
# a = list_1 + list_2
# a.sort()
# print(a)

# def list(a, b):
#     return a + b
# s.sort()
# s = list(a=[1,2,4,6], b=[3,7,8,5])
# print(s)

# 3. Вам предоставляется строка, представляющая запись посещаемости учащегося, где каждый символ означает, отсутствовал,
# опоздал или присутствовал в этот день. Запись содержит только следующие три символа: А отсустовал, L опоздал,
# P присуствовал
# Студент имеет право на получение стипендии, если он соответствует обоим следующим критериям:
# студент отсутствовал в общей сложности менее 2 дней.'A'
# Студент никогда не опаздывал () в течение 3 и более дней.'L'
# Если студент имеет право на стипендию True, False если не имеет
# сделать через функцию
# Gleb = "P, P, L, A, L"
# a = Gleb.count("A")
# b = Gleb.count("L")
# c = Gleb.count("P")
# if a < 2 and b < 3:
#     print("True")
# else:
#     print("False")
# print()

# 4. даны скобки, проверить правильно ли они закрываются либо открываются
# a = "()[]"
# if "()" in a or "[]" in a or "{}" in a:
#     print("True")
# else:
#     print("False")

# не првильно
# def skobki(a):
#     if "()" in a or "[]" in a or "{}" in a:
#         print("True")
#     else:
#         print("False")
# b = skobki(a="([]")

# 5. найти длину последнего слова в строке
# a = "Hello world za"
# b = a.split()
# c = b[-1]
# print(len(c))

# def lenght(a):
#     schet = a.split()
#     if schet:
#         return len(schet[-1])
# q = lenght(a="hello world")
# print(q)

# 6. показать индекс переменной, если ее нету показать индекс где бы она была
# a = [0,1,3,5,6,7]
# b = 2
# if b not in a:
#     a.append(b)
#     a.sort()
#     index = a.index(b)
#     print(index)
# elif b in a:
#     index = a.index(b)
#     print(index)

# убрать сорт убрать повторяющиеся строки в функции
# def chislo(a,b):
#     if b not in a:
#         a.append(b)
#         a.sort()
#         index=a.index(b)
#         return index
#     elif b in a:
#         index=a.index(b)
#         return index
# q = chislo(a=[1,3,4,5], b=6)
# print(q)

# сделать еще 5 задач и переделать эти!!!

