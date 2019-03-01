'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя
набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого
абитуриента выводит его среднюю оценку по этим трём предметам на отдельной
строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы
по математике, физике и русскому языку по всем абитуриентам
'''
import re
 
with open ('C:/Users/user/Desktop/dataset_3363_4.txt','r') as f:
    read_data = f.read()
    data = []
    data1 = []
    for i in read_data.split(";"):
        data += [i]
 
    for j in data:
        if re.search(r"\D", j) != None:
            j = re.sub(r"\D", "", j)
        try:
            int(j)
            data1 += [j]
        except:
            pass
    print(data1)
    first,second,third = 0,0,0
    namber_of_student = int((len(data1)) / 3)
    for i in range(namber_of_student):
        first += int(data1[0 + 3 * int(i)])
        second += int(data1[1 + 3 * int(i)])
        third += int(data1[2 + 3 * int(i)])
        q = (int(data1[0 + 3 * int(i)]) + int(data1[1 + 3 * int(i)]) + int(data1[2 + 3 * int(i)]))/3
        print(q)
    print(first/namber_of_student, second/namber_of_student, third/namber_of_student)
 
f.closed
