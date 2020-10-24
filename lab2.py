# # # text = 'Hello world'
# # # print(text.split(''))
# #
# # method isdigit проверяет все ли символы в строке цифры / ложь или правда
# numb=input('введите число')
# print(numb.isdigit())


# # method isalpha проверяет все ли символы в строке буква/ ложь или правда
# text=input('Введите букву')
# print(text.isalpha())


#method isalnum все ли символы в сроке цифры или буквы
# text=input('Введите букву')
# print(text.isalnum())
#
# string = 'Hello world'
# print(string.replace('o','fack',2))

#method isupper проверяет все ли символы в строке в верхнем регистре
#
# text = input('введите')
# print(text.islower())

#method isupper проверяет все ли символы в строке в нижнем регистре
# text = input('введите')
# print(text.islower())

#method is проверяет все ли символы в строке в табы или или пробелы
# text = input('введите')
# print(text.isspace())

#method isupper проверяет является ли строка заголовкоv
# text1='hello world'
# text2='Hello World'
# print(text1.istitle())
# print(text2.istitle())

#method lower перевод текста на в нижный регистр
# text='HELLO WORLD'
# print(text.lower())

# #method lower перевод текста на в верхний регистр
# string='dnjnvjfjnf'
# print(string.upper())
# method startswith проверяет начинается ли строка с опр символов

# method endswith проверяет заканчиваетс ли  строка с опр символов
# text='hello world'
# print(text.endswith('h'))
#  method join склеивает строку из разных частей
# text= 'hello my name is Timson'
# text_splited=text.split()
# print(text_splited)
# text2='j'.join(text_splited)
# print(text2)
#method ord номер символа из таблицы ASCII
#print(ord('A'))

# method count считает количество символов которые мы передаем в скобках

# text='hello world timsnon'
# print(text.count('l'))
#  method stip , lstrip, rstrip удаляет пробелы в начале и в конце
# text='       dcbahbvb      '
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# metgod swapcase  Меняет регистр букв на противоположный
# text='Hello world'
# text2= 'hello world'
# print(text.swapcase())
# print(text2.swapcase())
 # chtp строки
# text = 'hello world'
# print(text[5:0:-2])

#
# text =input(' Введите Текст')
#
# if text==text[::-1]:
#     print('Текст читается одиноково')
# else:
#     print('Текст не читается одинаково')
#форматирвание строки
name= input('Введите свое имя')
age=input('Введите свой возраст')
print('Привет'+ name+' вам '+ age)
print("f Вас зовут {name}.Ваш возраст{age}.")