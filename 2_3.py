'''
Напишите программу, которая считывает список чисел lst из первой строки и
число x из второй строки, которая выводит все позиции, на которых встречается
число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию
абсолютного значения.
'''
a = [int(i) for i in input().split()]
b = int(input())
c = 0
for i in range (len(a)):
    if a[i] == b:
        c += 1
        print (i, end=' ')
if c == 0:
    print ('Отсутствует')
    
