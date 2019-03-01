'''
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая
исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
'''
import re
with open("C:/Users/user/Desktop/dataset_3363_2.txt") as file:
    s=file.readline().strip()
    s=re.split("(\d+)", s)[:-1]
    out=open("C:/Users/user/Desktop/output.txt",'w')
    for i in range(len(s)):
        if i%2==0:
            output=s[i]*int(s[i+1])
            print(output)
            out.write(output + '')
        else:
            continue
out.close()
