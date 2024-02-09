# вот все методы словаря

# Методы для доступа к элементам словаря

# 1. Метод get() для получения значения элемента словаря по указанному ключу
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
# count = my_dict.get('banana')
# print(count)  # Вывод: 5
#
# count = my_dict.get('orange')
# print(count)  # Вывод: None
#
# count = my_dict.get('orange', 0)
# print(count)  # Вывод: 0

# 2.Метод setdefault() для получения значение элемента словаря по указанному ключу и добавления нового
# элемента, если ключ отсутствует
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
# count = my_dict.setdefault('banana')
# print(count)  # Вывод: 5
#
# count = my_dict.setdefault('orange')
# print(count)  # Вывод: None
#
# count = my_dict.setdefault('avocado', 0)
# print(count)  # Вывод: 0
#
# print(my_dict)  # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2, 'orange': None, 'avocado': 0}

# 3.Метод keys() для получения списка всех ключей
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
#
# keys = my_dict.keys()
# print(keys)  # Вывод: dict_keys(['apple', 'banana', 'cherry'])
#
# key_list = list(keys)
# print(key_list)  # Вывод: ['apple', 'banana', 'cherry']

# 4.Метод values() для получения списка всех значений
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
#
# values = my_dict.values()
# print(values)  # Вывод: dict_values([3, 5, 2])
#
# value_list = list(values)
# print(value_list)  # Вывод: [3, 5, 2]

# 5.Метод items()  для получения списка пар (ключ, значение)
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
#
# items = my_dict.items()
# print(items)  # Вывод: dict_items([('apple', 3), ('banana', 5), ('cherry', 2)])
#
# item_list = list(items)
# print(item_list)  # Вывод: [('apple', 3), ('banana', 5), ('cherry', 2)]


# Методы для добавления,обновления и удаления элементов

# 1.Метод update() для обновления словаря путем добавления пар ключ-значение из другого словаря
#
# Обновление словаря с помощью другого словаря:
# my_dict = {'apple': 3, 'banana': 5}
# other_dict = {'cherry': 2, 'orange': 4}
# my_dict.update(other_dict)
# print(my_dict)  # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2, 'orange': 4}
# Обновление словаря с помощью последовательности пар ключ-значение:
# my_dict = {'apple': 3, 'banana': 5}
# my_dict.update([('cherry', 2), ('orange', 4)])
# print(my_dict)  # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2, 'orange': 4}
#
# Обратите внимание, если в словаре, который мы обновляем, уже есть ключ из другого словаря или последовательности пар
# ключ-значение, то его значение будет обновленно. Рассмотрим пример:
# my_dict = {'apple': 3, 'banana': 5}
# other_dict = {'apple': 7, 'orange': 4}
# my_dict.update(other_dict)
# print(my_dict)  # Вывод: {'apple': 7, 'banana': 5, 'orange': 4}

# 2.Метод pop() для удаления элемента по указанному ключу и возврата его значения
#
# Удаление элемента по ключу и возврат его значения:
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
# value = my_dict.pop('banana')
# print(value)  # Вывод: 5
# print(my_dict)  # Вывод: {'apple': 3, 'cherry': 2}
#
# Удаление элемента по ключу и возврат значения по умолчанию при отсутствии ключа:
# my_dict = {'apple': 3, 'cherry': 2}
# value = my_dict.pop('banana', 0)
# print(value)  # Вывод: 0
# print(my_dict)  # Вывод: {'apple': 3, 'cherry': 2}

# 3.Метод popitem() для удаления и возврата последней пары ключ-значение из словаря
# fruits = {'apple': 3, 'banana': 5, 'cherry': 2}
# last_fruit = fruits.popitem()
# print(last_fruit)  # ('cherry', 2)
# print(fruits)  # {'apple': 3, 'banana': 5}

# 4.Метод clear() для удаления всех элементов из словаря
# my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
# my_dict.clear()
# print(my_dict)  # Вывод: {}

# 5.Метод copy() для создания поверхностной копии словаря
# original_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
# copied_dict = original_dict.copy()
# print(original_dict)  # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2}
# print(copied_dict)    # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2}
# # Изменяем оригинальный словарь
# original_dict['banana'] = 10
# print(original_dict)  # Вывод: {'apple': 3, 'banana': 10, 'cherry': 2}
# print(copied_dict)    # Вывод: {'apple': 3, 'banana': 5, 'cherry': 2}
