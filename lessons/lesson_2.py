# методы есть у всех изменяемых типов данных и строк


# питон - ссылочный язык (в питоне все является ссылками)
# a = 5
# print(id(a))
# b = 5
# print(id(b))

# объект существует в оператвивной памяти, пока к нему ведет хотя бы одна ссылка
# оператор del удаляет ссылку к объекту
# del a

# a = [1,2,3]
# b = [1,2,3]
# print(id(a[0]))
# print(id(b[0]))

# a = (1,2,3)
# b = (1,2,3)
# print(id(a))
# print(id(b))

# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
# del a
# print(b)

# a,b,c = 1,2,3
# print(a,b,c)

# словари основываются на структуре данных хеш-таблица

# хеш - это криптографический процесс кодирования данных с помощью какого-то алгоритма

# hash функия в питоне принимает только неизменяемые типы данных

# print({1,2,3,4,5,6,7,8,9,10})
# print(hash(1))

# порядок с set выстраивается от значения hash
# print({"a", "b", "c"})
# print(hash("a"))
# print(hash("b"))
# print(hash("c"))

# a = "1 2 3"
# print(hash(a))
# b = "1 2 3"
# print(hash(b))

# алгоритм хеширования живет один цикл программы, потом меняется
# оператор is проверяет является ли объект одинаковым в оперативной памяти(== проверяет значения, а is объект)
# print([1,2,3] is [1,2,3])

# ДЗ посмотреть и выписать все методы которые что-то возвращают и не возвращают,
# посмотреть все методы сетов, словарей, и строк
# по поводу hash в интернете НИЧЕГО не смотреть

# колизия - это когда хеш от разных ключей является одинаковым, решается колизия
# методом пробирования(когда в таблицу под ячейку записывется значение, и сравнения происходят на уровне питона)
