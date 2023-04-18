# # a=15
# # print(a)
# # print(id(a))
# # b = 15
# # print(b)
# # print(id(b))
# # print(type(a))
# # lesson1=14.4
# # # print(type(lesson1))
# # jf = True
# # print(type(jf))
# d='jon'
# print(f"hello {d}")
# name = input('please enter user name')
# age = int(input("Enter your age"))
# print(f"Hello, {name}. Your age is {age}. Password: \"password\"")
# print("Hello," + ' ' + name)
# number = int(input('Input any number'))
# print(number**2)
# num = 1
# print(bool(num))
# num3 = 0
# print(bool(num3))
# name = None
# print(type(name))
# # print('Hello world')
# # user_name = input('Input User Name')
# # print(f'Hello, {user_name}!')
# a = int(input('Input number_1'))
# b= int(input('Input number_2'))
# print('Result = ',a**b)
# print('*******')
# print('*     *')
# print('*     *')
# print('*******')
# print('*******\n*     *\n*     *\n*******', 'COOOL',sep='!',end= '\n')
# print(0.1+0.1+0.1)
# text = '*******\n*     *\n*     *\n*******'
# print(len(text))
# print("n"in text)
# text = '123456789'
# print(len(text))
# print(text[1])
# print(4**0.5)
# a, b, c = map('input', int, input().split())
# print(a, b, c, sep = '\')
# health = int(input("Input characteur,s health"))
# if health > 0:
#     print('True')
# else:
#     print ('False')
# number = int(input('input number to ferify is it even or odd'))
# if (number % 2) == 0:
#     print(number,' is even')
# else:
#     print(number, 'is odd')
# import i as i

# text = input('ВВедите текст для трансляции')
# count = int(input('Введите количество повторений текста'))
# # i = 0
# # while i < count:
# #     print(text)
# #     i = i + 1
# #     print(i)
#
#
# print((text + '\n')*count)

# num_1 = 0
# num_2 = 0
# import sys
# try:
#     num_1 = int(input('Введите число N1: '))
#     num_2 = int(input('Введите число N2: '))
# except ValueError:
#     print('Вы ввели не число!!!')
#     sys.exit()
#     operator = input('Введите арифметическую функцию')
# if operator not in '+-/*"//"%':
#     print('Вы ввели не функцию!!!')
#     sys.exit()
# if num_2 == 0 and operator == '/':
#     try:
#         result = num_1 / num_2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         sys.exit()
# elif num_2 == 0 and operator == '//':
#     try:
#         result = num_1 / num_2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         sys.exit()
# elif num_2 == 0 and operator == '%':
#     try:
#         result = num_1 / num_2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         sys.exit()
# elif operator == '+':
#     result = num_1 + num_2
#     print(f'Сумма {num_1} и {num_2} равна {result}')
# elif operator == '-':
#     result = num_1 - num_2
#     print(f' Разница {num_1} и {num_2}  равна {result}')
# elif operator == '*':
#     result = num_1 * num_2
#     print(f'Произведение {num_1} и {num_2} равно {result}')
# elif operator == '%':
#     result = num_1 % num_2
#     print(f'Остаток от деления {num_2} на {num_1} равен {result}')
# elif operator == '//':
#     result = num_1 // num_2
#     print(f'{num_1} делится на {num_2} {result} раз(а)')
# else:
#     result = num_1 / num_2
#     print(f'Частное {num_1} и {num_2} равно {result}')
# print(f' {num_1}{operator}{num_2} = {result}')
# #
# w1 = 'Юля'
# print(f"{s} - {(s.replace('Ю','Пу'))}")
# w2 = 'hello wold'
# # print(w2.count('el',0,5))
# w3 = 'Ivan Ivan Ivan Ivan'
# print(w3.split(' ', maxsplit = 2))
# w4 = '1111'
# print(w4.split("1"))
# # print('&'.join(w4))
# w5 = '    123HI123     '
# print(w5.strip().strip('123'))
# w6 = '110100101010010101010101'
# print(w6.find('0', 0, 20))
# print(w6.index('2'))
# w7 = 'ivan IVAN'
# print(1,w7.upper())
# print(2,w7.lower())
# print(3,w7.title())
# print(4,w7.capitalize())
# print(5,w7.swapcase())
# print(w7.isupper()) # все состоит из заглавных#
# print(w7.isdigit()) # cостоит из чисел
# print(w7.isalfa())
# sentence = 'Hello World'
# my_list = [1, 'Zhenya', 2.0, True, False]
# print(my_list.index(2.0))
# my_list.append(sentence)
# my_list.insert(1, sentence)
# print(my_list)
# print(len(my_list))
# my_list = [1, 2, 3, 4, 5, [1, 2, 3, ['a', 'b', 'c', 'd']]]
# print(my_list[-1][-1][1])
# # print(sum(my_list))
# print(min(my_list))
# print(max(my_list))
# my_list = [1, 2, 3, 4, 5]
# new_list = list()
# for a in my_list:
#     if a % 2 != 0:
#         new_list.append(a)
#     else:
#         new_list.append(a**2)
# print(new_list)
# new_list = [a for a in my_list if a % 2 ]
# new_list = [a**2 for a in my_list if a % 2 == 0 ]
# print(new_list)
# my_tuple = 1, 2, 3 ,4 ,5,2.9
# print (my_tuple)
# tuple1 = tuple([(i+1) for i in my_tuple if isinstance(i, int)])
# print(tuple1)
# t = 'apple', ['ananas', 'banana'], 'pine'
# print(t)
# t[1][0] = 'cherry'
# t[1] = 'cherry'
# print(t)
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(1, 2, 3))
# def func(*args):
#     l =[]
#     for num in args:
#         l.append(num/2)
#     return l
#     print(l)
# print(func(2, 4 , 6 , 8, 10))

# my_list = ['a', 'b', [1, 2, 3], 'd']
# list1 = my_list[2]
# print(*list1, sep = '\n')
# print(my_list[2])
# print(*list1)
# # print(my_list[2][0],my_list[2][1], my_list[2][2], sep = ', ')

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36.0, 100]
# a= 0
# for num in list_1:
#     if type(num) == int:
#         a=a+num
# print(a)
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36.0, 100]
# list_2=[]
# for num in list_1:
#     print(type(num))
#     if type(num) == str :
#         if 'a' in num:
#             list_2.append(num)
# print(list_2)
# list_2 = [a for a in list_1 if  'a' in str(a) ]
# list_2 = [a for a in list_1 if  'a' in str(a) ]
# print(list_2)
# list_animals = ['cat', 'dog', 'horse', 'cow']
# tuple_1 = tuple(list_animals)
# print(tuple_1)

# family_1 = input('Введите 1 семью').split(', ')
# family_2 = input('Введите 2 семью').split(', ')
# a = len(family_1)
# b = len( family_2)
# print(len(family_1))
# if a > b:
#     print(family_1)
# elif b < a:
#     print(family_2)
# elif a == b:
#     print('Equal')
# print(family_1, family_2)


# family_1 = input('Введите членов 1 семьи через ",":').split(',')
# family_2 = input('Введите членов 2 семьи через "," :').split(',')
# # a = len(family_1)
# # b = len( family_2)
# if len(family_1) > len( family_2):
#     print(family_1)
# elif len(family_1) < len( family_2):
#     print(family_2)
# # else :
# #     print('Equal')
# # print(len(family_1), len( family_2))
# film = {'title' : 'Z',
#     'director' : 'Jz',
# 	'year' : 2000,
# 	'budget' : 1000000,
# 	'main_actor' : 'Kloony',
# 	'slogan' : 'What tha fuck?!?!'}
# # print( *film.keys())
# # print( *film.values())
# # print(*(film.items()))
# for key, value in sorted(film.items()):
#     print(key,':', value,end = ', ')

#
# a=0
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# # print(*my_dictionary.values())
# # print(sum(my_dictionary.values()))
# for key, value in  my_dictionary.items():
#     print(a + value)
#     a = a + value

# lst = [1, 2, 3, 4, 5, 3, 2, 1]
# lst2 = []
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# new_list = list(set([1, 2, 3, 4, 5, 3, 2, 1]))
#
# print(new_list)
# new_list = {1, 2, 3, 4, 5, 3, 2, 1}
# print(new_list)

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1 &set2)
# print(set1.intersection(set2))
# print(set1^set2)
# print(set1.symmetric_difference(set2))
# print(set1>=set2)
# print(set1<=set2)
# print(set1.issubset(set2))
# print(set1.issuperset(set2))

# num_1 = 0
# num_2 = 0
# import sys
# flag = True
# while flag == True:
#     try:
#         num_1 = int(input('Введите число N1: '))
#         num_2 = int(input('Введите число N2: '))
#         operator = input('Введите арифметическую функцию')
#         if operator not in '+-/*"//"%':
#             print('Вы ввели не функцию!!!')
#         elif operator == '+':
#             result = num_1 + num_2
#             print(f'Сумма {num_1} и {num_2} равна {result}')
#         elif operator == '-':
#             result = num_1 - num_2
#             print(f'Разница {num_1} и {num_2} равна {result}')
#         elif operator == '*':
#             result = num_1 * num_2
#             print(f'Произведение {num_1} и {num_2} равна {result}')
#         elif operator == '%':
#             result = num_1 % num_2
#             print(f'Остаток от деления {num_1} и {num_2} равна {result}')
#         elif operator == '//':
#             result = num_1 // num_2
#             print(f' {num_1} делится на  {num_2} {result} раза ')
#         else:
#             result = num_1 / num_2
#             print(f'Частное {num_1} и {num_2} равно {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#     except ValueError:
#         print('вы ввели не число, повторите ввод')
#     txt = input('Если хотите продолжить нажмите Enter, для выхода нажмите N')
#     if txt == 'N' or txt == 'n' or txt == 'т' or txt == 'Т':
#         flag = False
#
        
#     if operator not in '+-/*"//"%':
#         print('Вы ввели не функцию!!!')
#         sys.exit()
#     if num_2 == 0 and operator == '/':
#         try:
#            result = num_1 / num_2
#         except ZeroDivisionError:
#            print('На ноль делить нельзя')
#            sys.exit()
#     elif num_2 == 0 and operator == '//':
#         try:
#            result = num_1 // num_2
#         except ZeroDivisionError:
#            print('На ноль делить нельзя')
#            sys.exit()
#     elif num_2 == 0 and operator == '%':
#         try:
#             result = num_1 % num_2
#         except ZeroDivisionError:
#            print('На ноль делить нельзя')
#            sys.exit()
#     elif operator == '+':
#         result = num_1 + num_2
#         print(f'Сумма {num_1} и {num_2} равна {result}')
#     elif operator == '-':
#         result = num_1 - num_2
#         print(f' Разница {num_1} и {num_2}  равна {result}')
#     elif operator == '*':
#         result = num_1 * num_2
#         print(f'Произведение {num_1} и {num_2} равно {result}')
#     elif operator == '%':
#         result = num_1 % num_2
#         print(f'Остаток от деления {num_2} на {num_1} равен {result}')
#     elif operator == '//':
#         result = num_1 // num_2
#         print(f'{num_1} делится на {num_2} {result} раз(а)')
#     else:
#         result = num_1 / num_2
#         print(f'Частное {num_1} и {num_2} равно {result}')
#     txt = input('Если хотите продолжить нажмите Enter, для выхода нажмите N')
# except ValueError:
#     print('Вы ввели не число!!!')
#     # sys.exit()
# if txt == 'N' or txt == 'n' or txt == 'т' or txt == 'Т':
#     flag = False
# def vozvedenie_v_stepen(a, n):
#     return (a ** n)
# print(vozvedenie_v_stepen(2, 2))
# lst = [1,2,3,'ddd']
# lst2=[]
# for i in lst:
#     if isinstance(i,int):
#         lst2.append(i)
# print (lst2)
# new = list(filter(lambda x: (x ** x) and type(x) != str , lst))
# new = list(map(lambda x: type(x) != str and vozvedenie_v_stepen(x, x), lst))
# new = list(filter(lambda x: x**x if isinstance(x, int) else None, lst))
# #
# print(*new)
#
# def square(a):
#     s = a ** 2
#     p = 4 * a
#     d = round((2 * a ** 2) ** 0.5, 3)
#     return s, p, d
# print(tuple(square (2)))
# print(square (2))

# def anketa(datas):
#     a = input('введите ключ, если не хотите продолжить, введите stop')
#     b = input('введите значение')
#     datas = dict (a=b)
#     return datas
# print(anketa(datas))
# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# employee(last_name='Popov', name='Max', age=40, position='web developer')


def anketa(**dan):
    for Name, Value in dan.items():
        print(f'{Name}-{Value}')
anketa(name='John', last_name = 'Smith', age = 35, position= 'web developer\ ')пше