# Методы которые что-то возвращают

# 1.  union -возвращает объединение множеств
# a = {1,2,3}
# b = {3,4,5}
# c = a.union(b)
# print(c)

# 2. intersection - возвращает пересечение множеств
# a = {1,2,3}
# b = {3,4,5}
# c = a.intersection(b)
# print(c)

# 3. difference - возвращает разницу между множествами
# a = {1,2,3}
# b = {3,4,5}
# c = a.difference(b)
# print(c)

# 4. symmetric_difference - возвращает симметрическую разницу между множествами
# a = {1,2,3}
# b = {3,4,5}
# c = a.symmetric_difference(b)
# print(c)

# 5. copy - возвращает копию множества
# a = {1,2,3}
# b = a.copy()
# print(b)

# 6. intersection_update - обновляет множество, оставляя в нем только элементы, присуствующие во всех множествах
# a = {1,2,3}
# b = {3,4,5}
# a.intersection_update(b)
# print(a)

# 7. difference_update - обновляет множество, удаляя из него элементы, присуствующие в других множествах
# a = {1,2,3}
# b = {3,4,5}
# a.difference_update(b)
# print(a)

# 8. symmetric_difference_update - обновляет множество, оставляя в нем элементы, присуствующие только в
# одном из множеств
# a = {1,2,3}
# b = {3,4,5}
# a.symmetric_difference_update(b)
# print(a)


# МЕТОДЫ КОТОРЫЕ  НИЧЕГО НЕ ВОЗВРАЩАЮТ

# 1. add - добавляет элемент в множество
# a = {1,2,3}
# a.add(4)
# print(a)

# 2. remove - удаляет элемент из множества, если элемент не найден - вызывает ошибку
# a = {1,2,5,3}
# a.remove(5)
# print(a)

# 3. discard - удаляет элемент из множества, если он присуствует
# a = {1,2,5,3}
# a.discard(5)
# print(a)

# 4. pop - удаляет и возвращает произвольный элемент из множества; вызывает ошибку если множество пусто
# a = {1,2,3}
# b = a.pop()
# print(b)

# 5. clear - удаляет все элементы из множества
# a = {1,2,3}
# a.clear()
# print(a)

# 6. update - добавляет элементы из других множеств в текущее множество
# a = {1,2,3}
# b = {3,4,5}
# a.update(b)
# print(a)