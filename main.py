import datetime as dt
import sys

def printHeader():
    print('===========================')
    print('#\t TERMINOTE \t#')
    print('Date :',dt.datetime.today().isoformat()[:10])
    print('===========================')    

def mainMenu(buffer:int = 0):
    printHeader()
    print('(1) Add Note\n(2) View Notes\n(3) Clear Notes\n(4) quit')
    choice = input('')
    if choice.isdecimal():
        choice = int(choice)
    match choice:
        case 1:
            addNote()
        case 2:
            listNotes()
        case 3:
            clearNotes()
        case 4:
            sys.exit()
        case _:
            print('INVALID INPUT')
            if buffer >= 3:
                print('Too many Invalid Inputs.\nClosing Program...')
                sys.exit()
            mainMenu(buffer+1)

def addNote():
    now = dt.datetime.today().isoformat()
    entry = input(f'Add Note | {now} :\n')
    with open('tasks.txt','a') as f:
        f.write(f'{entry}\n')
    listNotes()

def listNotes():
    length = 0
    print('======Tasks=======')
    with open('tasks.txt','r') as f:
        n = 0
        for i in f.readlines():
            n+=1 
            print(f'{n}) {i}')
        length = n
    order = input(f'[1-{length}] to clear a task | [Q] to quit | [A] to add\n')
    if order.isdecimal():
        index = int(order)
        if index <= 0 or index > length:
            print(f'Task does not exist at index {index}')
            return
        removeNote(index)
    elif order.lower() == 'q':
        sys.exit()
    elif order.lower() == 'a':
        addNote()

def clearNotes():
    with open('tasks.txt','w') as f:
        f.write('')
    print('All tasks cleared!\n')

def removeNote(lineN: int):
    rf = open('tasks.txt','r')
    lineList = rf.readlines()
    rf.close()
    if lineN > len(lineList) or lineN <= 0:
        print('##Invalid Note Index##\n Returning to menu...\n')
        return
    lineList.pop(lineN-1)
    with open('tasks.txt','w') as wf:
        wf.write(''.join(lineList))
    print(f'task {lineN} cleared!\n')

def main():
    try: open('tasks.txt','r')
    except FileNotFoundError:
        print('initializing files...')
        f= open('tasks.txt','w+')
        f.close()
    while True:
        mainMenu()

if __name__ == '__main__':
    main()