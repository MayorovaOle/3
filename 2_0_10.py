'''
Напишите программу, которая принимает на вход список чисел в одной строке и
выводит на экран в одну строку значения, которые повторяются в нём более одного
раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
a = [int(i) for i in input().split()]
a.sort()
b = []
for i in range (1, len(a)):
    if a[i] == a[i-1]:
        if a[i] not in b:
            b.append (a[i])
for i in range (len(b)):
    print(b[i], end=' ')
    
        
