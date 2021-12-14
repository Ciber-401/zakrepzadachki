# Задание 10:
#     Дано
dict_one = {'a':1, 'b':2, 'c':3}

dict_two = {'d':4, 'e':5, 'f':6}

dict_two = {'g':7, 'h':8, 'i':9}

slovary = (dict_one,dict_two,dict_two)

dict_four = []
#     С помощью цикла for необходимо собрать три первых словаря в словарь dict_four
for i in slovary:

 dict_four.append(slovary)

 print(dict_four)
#     Подсказка: Для удобства итерации, первые три словаря можно
#     записать в кортеж (dict_one, dict_two, dict_three