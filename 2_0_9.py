'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его
соседей. Для элементов списка, являющихся крайними, одним из соседей считается
элемент, находящий на противоположном конце этого списка. Например, если на
вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7"
(без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными
пробелом.
'''
a = [int(i) for i in input().split()]
c = len(a)
s = 0
if c != 1:
    for b in range (c-1):
        s = a[b-1] + a[b+1]
        print (s, end=' ')
    s = a[c-2] + a[0]
    print (s, end=' ')
else:
    s = a[0]
    print(s,end=' ')
    

