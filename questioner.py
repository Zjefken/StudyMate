from random import randint
import os
from time import sleep

def cls(time):
    sleep(time)
    os.system('cls')

def importData():
    global datalist
    filename = input('Filename(without .txt) >>>')
    filename += '.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        datalist = file.readlines()
        for i in range(len(datalist)):
            datalist[i]=datalist[i].replace('\n','')
            datalist[i]=datalist[i].split(',')
            datalist[i][1]=datalist[i][1].strip()
        file.close()
    
def askData():
    global datalist
    while len(datalist) != 0:
        num = randint(0, len(datalist) - 1)
        question = datalist[num][0]
        answer = datalist[num][1]
        givenanswer = input(question + ' >>>')
        if givenanswer == answer:
            print('Correct!')
            datalist.pop(num)
            cls(2)
            if len(datalist) > 1:
                print(str(len(datalist)) + ' questions left!')
            elif len(datalist) == 1:
                print('Last question!')
        else:
            print('Wrong!')
            print(answer + ' was the correct answer.')
            clstime = len(answer) / 6
            cls(2 + clstime)
            if len(datalist) > 1:
                print(str(len(datalist)) + ' questions left!')
            elif len(datalist) == 1:
                print('Last question!')
    input('Press enter to exit...')

importData()
askData()
