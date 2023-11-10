import os

def cls():
    os.system('cls')

def createText():
    global text
    list = []
    choice = input('Template (yes or no)? >>> ')
    if choice == 'no':
        for i in range(1, int(input('How many questions? >>> ')) + 1):
            print(i)
            question = input('Question? >>> ').strip()
            answer = input('Answer? >>> ').strip()
            combination = ', '.join([question, answer])
            list.append(combination)
            cls()
    elif choice == 'yes':
        with open('Templates/' + input('Filename? >>> ') + '.txt', 'r', encoding='utf-8') as file:
            template = file.read()
            template = template.split(',')
            file.close()
        for i in range(0, len(template)):
            template[i] = template[i].strip()
            answer = input(template[i] + ' answer? >>> ').strip()
            combination = ', '.join([template[i], answer])
            list.append(combination)
            cls()
    else:
        exit()
    text = '\n'.join(list)
    print(text)

def createFile():
    global text
    fname = input('Filename? >>> ')
    with open(fname + '.txt', 'w', encoding='utf-8') as file:
        file.write(text)
        file.close()

createText()
createFile()
input('Press enter to exit...')