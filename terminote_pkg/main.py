import datetime as dt

def printHeader():
    print('===========================')
    print('#\t TERMINOTE \t#')
    print('Date : ',dt.datetime.today().isoformat())
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
            quit()
        case _:
            print('INVALID INPUT')
            if buffer >= 3:
                print('Too many Invalid Inputs.\nClosing Program...')
                quit()
            mainMenu(buffer+1)
    loop = input('[Q] to quit | [ANY] to return to menu')
    if loop != 'q':
        mainMenu()
    else:
        quit()

def addNote():
    now = dt.datetime.today().isoformat()
    entry = input(f'Add Note | {now} :\n')
    with open('tasks.txt','a') as f:
        f.write(f'{entry}\n')
    listNotes()

def listNotes():
    print('======Tasks=======')
    with open('tasks.txt','r') as f:
        n = 1
        for i in f.readlines():
            print(f'{n}) {i}')
            n+=1

def clearNotes():
    with open('tasks.txt','w') as f:
        f.write('')

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

def main():
    try: open('tasks.txt','r')
    except FileNotFoundError:
        print('initializing files...')
        f= open('tasks.txt','w+')
        f.close()
    mainMenu()

if __name__ == '__main__':
    main()