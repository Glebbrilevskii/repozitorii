# функции в питоне объявляются через ключевое слово def, функция всегда что-то возвращает
# функция это участок кода который мы можем вызывать где хотим и сколько хотим и он будет выполнятся
# def hello_world():
#     return "hello world"
# a = hello_world()
# b = hello_world()
# c = hello_world()
# print(a, b, c)
# ключевое слово return может вызываться только в теле функции и после return ставиться объект который функция
# должна вернуть, после return ничего не выполняется (функция завершает работу), в функции выполниться только один return
# функция может принимать аргументы - позиционные и именованные, они идут по порядку
# def sum_to_numbers(number_1, number_2):
#     return number_1 + number_2
# a = sum_to_numbers(10, 20)
# b = sum_to_numbers(number_1=20, number_2=30)
# print(a)
# print(b)
# определили 2 пoзиционных аргумента

# def calculet(number_1, number_2, number_3=10):# после именнованых аргументов мы не можем прописать позиционные
#     return number_1 * number_2 * number_3
# a = calculet(20,30, 40)
# print(a)

# неограниченное кол-во позиционных и именованых аргументов *args, **kwargs
# def calculet(*args, **kwargs):
#     print(args, kwargs)
# a = calculet(1,2,3,4,5,6,7,8,9,10, b=1, c=2, w=3, e=4)

# написать функцию полноценного калькулятора
# посмотреть видео по гит, настроить его себе

# def calculator(chislo_1, chislo_2, znak):
#     return chislo_1 // chislo_2
# a = calculator(chislo_1=8, chislo_2=2, znak="//")
# print(a)


# a = int(input())
# b = input()
# c = int(input())
# if b == "+":
#     print(a + c)
# if b == "/":
#     print(a // c)
# if b == "*":
#     print(a * c)
# if b == "-":
#     print(a - c)

