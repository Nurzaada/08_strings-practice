from pprint import pprint
# # 1 Создать две строки и выполнить конкатенацию.
# str_1 = 'text'
# str_2 = 'one more text'

# # Конкатенация строк с пробелом между ними
# print(str_1 + ' ' + str_2)

# # 2 Повторить короткую строку несколько раз.
# str_short = 'abc'

# # Повторение строки три раза
# print(str_short * 3)

# # 3 Вывести первый и последний символ строки.
# str_3 = 'Hello World!'

# # Вывод первого символа строки
# print(str_3[0])
# # Вывод последнего символа строки
# print(str_3[-1])
# # Вывод каждого второго символа строки
# print(str_3[::2]) 
# # Вывод строки в обратном порядке
# print(str_3[::-1])

# # Преобразовать строку в верхний регистр и в нижний регистр.
# str_5 = 'absdFH'
# # Преобразование строки в верхний регистр
# print(str_5.upper())
# # Преобразование строки в нижний регистр
# print(str_5.lower())

# str_6 = ' cahu '
# # Удаление пробелов в начале и в конце строки
# print(str_6.strip())
# # Вывод строки без изменений
# print(str_6)

# # Пример строки для демонстрации
# print('asdasdasd')

# str_7 = 'dosca'
# # Поиск первого вхождения символа 'o'
# print(str_7.find('o'))
# # Поиск первого вхождения символа 'a'
# print(str_7.find('a'))

# str_8 = 'Bishkek, Moscow 183'
# # Замена 'Moscow' на 'Toktogul'
# str_8 = str_8.replace('Moscow', 'Toktogul')

# print(str_8)
# # Замена 'Bishkek' на 'Osh'
# print(str_8.replace('Bishkek', 'Osh'))

# '''
# #### 1. Шифр Цезаря  
# Задание:  
# Напишите программу, которая шифрует строку с помощью шифра Цезаря.
# Шифр Цезаря — это сдвиг каждой буквы на определенное количество позиций в алфавите. Например, сдвиг на 3:  
# - A -> D  
# - B -> E  
# - Z -> C (алфавит зациклен).  

# Пример:  
# Вход: "Hello, World!", сдвиг: 3  
# Выход: "Khoor, Zruog!"  
# '''

# # Пример словаря для шифрования
# code = {
#     'A': 'C',
#     'B': 'Z',
#     'C': 'E',
#     'D': 'H',
#     'E': 'L',
#     'F': 'O',
# }

# text = 'DCEEF'
# uncoded_text = ''
# # Проход по каждому символу в тексте
# for i in text:
#     print(i)
#     # Вывод зашифрованного символа
#     print(code[i])
#     # Добавление зашифрованного символа к результату
#     uncoded_text += code[i]
# # Вывод зашифрованного текста
# print(uncoded_text)

# text='Nazira jana Myrzaym'
# # Вывод исходного текста
# print(text)
# # Преобразование текста в верхний регистр
# print(text.upper())
# # Вывод текста в обратном порядке
# print(text[::-1])

# # Разделение текста на слова
# print(text.split())
# uncodent_text = ''
# # Проход по каждому слову в тексте
# for i in text.split():
#     # Вывод первого символа слова
#     print(i[0])
#     # Добавление первого символа слова к результату
#     uncodent_text += (i[0])
# # Вывод результата
# print(uncodent_text)

name = " Nazira Jumagul"
letters = {
}

for i in name:
    print(f'Letter: {i}')
    if letters.get(i):
        print(f'Letter {i} already exists')
        letters[i] += 1
    else:
        print(f'Letter {i} is new')
        letters[i] = 1
pprint(letters)
# # Подсчет количества вхождений символа 'a'
# print(name.count("a"))
# # Замена пробелов на подчеркивания
# print(name.replace(" ","_"))




