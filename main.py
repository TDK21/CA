# Console ca app, Author: TDK21
import matplotlib.pyplot as plt
import numpy as np
import os
# question block
q1 = "Укажите ваш пол:\n1 - мужской\n2 - женский"
q2 = "Укажите ваш возраст:\n1 - меньше 18\n2 - больше 18"
q3 = "Укажите ваш доход:\n1 - <60000\n2 - >60000"
q4 = "Сколько вы употребляете сахара?:\n1 - мало\n2 - много"
q5 = "Это ваше первое посещение?:\n1 - да\n2 - нет"
q6 = "Насколько хорошо вы ухаживаете за своими зубами?:\n1 - хорошо, частая чистка\n2 - плохо, редкая чистка"
q7 = "Цель посещения?:\n1 - острая боль\n2 - профилактика"
q_block = [q1, q2, q3, q4, q5, q6, q7]
title_block = ["Пол", "Возраст", "Доход", "Употребление сахара", "Первое посещение", "Уход за зубами", "Цель посещения"]
answ_list = []
answ_block = [0, 0, 0, 0, 0, 0, 0]
mylabels = ["Мужской", "Женский", "Меньше 18", "Больше 18", "Меньше 60к", "Больше 60к", "Мало", "Много", "Да", "Нет", "Хорошо, частая чистка", "Плохо, редкая чистка", "Острая боль", "Профилактика"]
curlabels = []
pie_colors=(["green", "blue"])

def getAnswers():
    j = 0
    for i in q_block:
        print(i)
        answer = input()
        answ_list.append(answer)
        if (answer == "1"):
            answ_block[j] += 1
        else:
            answ_block[j] -= 1
        j += 1
    os.system('CLS')


def diagramsPrint():
    j = 0
    alpha = 0
    for i in answ_block:
        res = answ_block[i]
        if (res > 0):
            minor = 7 - res
            major = 7 + res
        if (res < 0):
            minor = 7 + res
            major = 7 - res
        else:
            minor = 7
            major = 7
        curlabels.append(mylabels[j])
        curlabels.append(mylabels[j+1])
        y = np.array([minor, major])
        plt.title(title_block[alpha])
        plt.pie(y, labels=curlabels, autopct='%1.1f%%', shadow=True, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, colors=pie_colors)
        plt.show()
        j += 2
        alpha += 1
        curlabels.clear()


if __name__ == '__main__':
    i = 0
    while (i < 10):
        getAnswers()
        i += 1
        answ_list = []
    diagramsPrint()
