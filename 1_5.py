'''
Напишите программу, которая получает на вход три целых числа, по одному
числу в строке, и выводит на консоль в три строки сначала максимальное,
потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''
a = int(input())
b = int(input())
c = int(input())
s = a + b + c
maxi = -10000
mini = 10000
if a >= maxi:
    maxi = a
if a <= mini:
    mini = a
if b >= maxi:
    maxi = b
if b <= mini:
    mini = b
if c >= maxi:
    maxi = c
if c <= mini:
    mini = c
print(maxi)
print(mini)
print(s - maxi - mini)
