# 1:
def sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    print(s)
sum(1234)


# # 2:
# def events_dol(a, b, c, d):
#     print((a + b + c + d) / 4)
# events_dol(2, 4, 6, 8)




# #5:
# def reverses(text):
#     print(text[::-1])
# reverses('com')


# #6:
# def word_microsoft(text):
#     words = text.split()
#     print(len(words))
# word_microsoft('Школа окончена')


# #7:
# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False






# #1:
# def hello(name):
#     print("Привет", name)
# hello('name')


# # 2:
# def add(a, b):
#     return a + b
# print(add(2, 3))


# #3:
# def co(mil):
#     return mil **2
# print(co(5))

# #4:
# def sip(nictoc):
#     return len(nictoc)
# ret = sip('python')
# print(ret)


# # 5:
# def op_sium(a, b):
#     if a > b:
#         print("больше")
#     elif a < b:
#         print('равны')
#     else:
#         print('числа равны')
# op_sium(5, 8)
# op_sium(7, 3)
# op_sium(4, 4)


# #6:
# def is_bib(cik):
#     if cik % 2 == 0:
#         return True
#     else:
#         return False
    

# #7:
# def faktorial(n):
#     for i in range(1, n):







# Задание другое совершенно! Группа = Backend StartUm
#7:
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# print(is_adult(32))

# #8:
# def max_num(a, b):
#     if a > b:
#         return "Большее из двух =", a
#     elif a < b:
#         return 'Большее из двух =', b
# print(max_num(2, 5))
# print(max_num(3, 1))

# # 9:
# def grade(score):
#         if score >= 90:
#             return 'Отлично!'
#         elif score >= 70:
#             return 'хорошо!'
#         else:
#             return 'плохо'
# # while True:
# score = int(input('Введите число для функции: '))
# print(grade(score))

# #10:
# def countdown(n):
#     for Youtube in range(n, 0, -1):
#         print(Youtube)
# num = int(input('введите число ваше '))
# print(countdown(num))


# #11:
# def count_even_numbers(numbers):
#     vol = 0
#     for i in numbers:
#         if i > 0:
#             vol += i
#     return vol
# print(count_even_numbers([-2, 5, 0, 3, -1]))

# #12:
def count_even_odd(numbers):
    e = 0
    c = 0
    for i in numbers:
        if i % 2 == 0:
            e += 1
        else:
            c += 1
    return e, c
print(count_even_odd([1, 2, 3, 7, 5]))

# #13:

# def average(numbers):
#     lor = 0
#     first = True # флаг для проверки есть ли элементы 
#     for num in numbers:
#         lor += num
#         first = False #есть элемент
    
#     if first: # если ни одного числа не было 
#         return 0
#     else:   # чтобы посчитать колличество пробежим еще раз
#         count = 0
#         for po in numbers:
#             count += 1
#         return lor / count
# print(average([2, 4, 6]))
# print(average([]))


# #14:
# def longest_word(words):
#     longest = ''
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest
# print(longest_word(['кот', 'собака', 'мышь']))
# print(longest_word(['яблоко', 'груша', 'банан']))

# #15:
# def factorial(n):
#     result = 1
#     for io in range(1, n + 1):
#         result *= io
#     return result
# print(factorial(5))
# print(factorial(0))


# #16:
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('level'))
# print(is_palindrome('python'))
# print(is_palindrome('радар'))

# #17:
# def square(n):
#     return n * n
# def sum_of_squares(numbers):
#     c = 0
#     for number in numbers:
#         c += square(number)
#     return c
# print(sum_of_squares([1, 2, 3]))

# #18:
# def common_element(list1, list2):
#     common = []
#     for it in list1:
#         if it in list2:
#             common.append(it)
#     return common
# print(common_element([1, 2, 3], [2, 3, 4]))
# print(common_element(['яблоко', 'груша'], ['банан', 'груша']))

# #19:
# def censor(text, bad_word):
#     return text.replace(bad_word, "***")
# print(censor("я учу pythom, или pythom легок", "pythom"))


# def vip(a, b):
#     return a + b

# res = vip(5.7, 9.4)
# vip('h', 'i')
# print(res)




# def minimals(l):
#     min = l[0]
#     for i in l:
#         if i < min:
#             min = i
#     print(min)
# nums = [1, 2, 4, 5, 6, 7, 8, 9, 10]
# minimals(nums)

 

# def add(*args):
#     return sum(args)

# print(add(1, 2, 3))
# print(add(10, 20))




# def day(username, age):
#     print(f'Hello {username}') 
#     print(f'Your age old: {age}')
#     print(n + 20)
# n = 1
# day('water', 10)
# day('lolicerotp', 10)

# def calculate(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
# final = calculate(100, 0.15)
# print(final)


# try:
#     def co(price, area):
#         z = price / area
#         print(z)
#     co(1, 0)
# except:
#     print("Ошибка на 0 нельзя делить")



