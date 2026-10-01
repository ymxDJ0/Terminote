import datetime as dt
import sys
import os

currentNotebook = ''

def printHeader():
    print('===========================')
    print('#\t TERMINOTE \t#')
    print('Date :',dt.datetime.today().isoformat()[:10])
    print('===========================')    

def mainMenu():
    printHeader()
    print(f"Current Notebook : {currentNotebook}")
    print('(1) View Notes\n(2) Manage Notebooks\n(3) quit')
    choice = input('')
    if choice.isdecimal():
        choice = int(choice)
    match choice:
        case 1:
            listNotes()
        case 2:
            listNotebooks()
        case 3:
            sys.exit()
        case _:
            listNotes()

def addNote(I : str = ''):
    now = dt.datetime.today().isoformat()
    if I != '':
        entry = I
    else:
        entry = input(f'Add Note | {now} :\n')
    with open(currentNotebook,'a') as f:
        f.write(f'{entry}\n')
    listNotes()

def listNotes():
    length = 0
    print('======Tasks=======')
    with open(currentNotebook,'r') as f:
        n = 0
        for i in f.readlines():
            n+=1 
            print(f'{n}) {i}')
        length = n
    order = input(f'[1-{length}] to clear a task | [help] for command | type to add a task\n')
    if len(order) > 1:
        if order.lower() == 'help':
            print(f'Commands:\n[1-{length}] to clear a task\n[clear] - clear all tasks\n[help] - show this message\n[q] - quit the program')
            listNotes()
        elif order.lower() == 'clear':
            clearNotes()
        else:
            addNote(order)
    elif order.isdecimal():
        index = int(order)
        if index <= 0 or index > length:
            print(f'Task does not exist at index {index}')
            return
        removeNote(index)
    elif order.lower() == 'q':
        sys.exit()

def clearNotes():
    with open(currentNotebook,'w') as f:
        f.write('')
    print('All tasks cleared!\n')

def removeNote(lineN: int):
    rf = open(currentNotebook,'r')
    lineList = rf.readlines()
    rf.close()
    if lineN > len(lineList) or lineN <= 0:
        print('##Invalid Note Index##\n Returning to menu...\n')
        return
    lineList.pop(lineN-1)
    with open(currentNotebook,'w') as wf:
        wf.write(''.join(lineList))
    print(f'task {lineN} cleared!\n')

def main():
    if not os.path.exists("notebooks.txt"):
        print('initializing files...')
        print('no notebooks found, let\'s create our first notebook!')
        createNotebook()
    listNotebooks()
    while True:
        mainMenu()

def listNotebooks():
    f = open('notebooks.txt','r')
    notebooks = [line.strip() for line in f.readlines()]
    f.close()
    print("input a number to select\n type 'new' to create a new notebook\n")
    for i, notebook in enumerate(notebooks, start=1):
        print(f"({i}) {notebook}")
    selection = input("")
    if selection.isdecimal():
        selection = notebooks[int(selection)-1]
        try:
            open(selection,"r").close()
        except FileNotFoundError:
            f = open(selection,'w+')
            f.close()
        global currentNotebook
        currentNotebook = selection
        return
    match selection.lower().strip():
        case 'new':
            createNotebook()
        case _ if selection.lower()[:4] == "new ":
            createNotebook(selection[4:].strip())
        case 'q':
            sys.exit()
        case _ if selection.lower()[:4] == "del " and len(selection) == 5:
            delNotebook(int(selection[4]))
        case 'help':
            print("[new (number)] - create a new notebook\n[del (number)] - delete a notebook\n[q] - quit the program")
            listNotebooks()
        case _:
            print("invalid Input, use a number to select a notebook or type (help) for commands")
            listNotebooks()
    
def createNotebook(n: str = ''):
    name = n
    if name == '':
        name = input('Enter Notebook Name: ')
    f= open(f'{name}.txt','w+')
    f.close()
    print(f'Notebook {name} created!\n')
    with open('notebooks.txt','a') as f:
        f.write(f'{name}.txt\n')

def delNotebook(n: int):
    f = open('notebooks.txt','r')
    notebooks = [line.strip() for line in f.readlines()]
    f.close()
    if n <= 0 or n > len(notebooks):
        print(f'Notebook does not exist at index {n}')
        return
    notebookToDelete = notebooks[n-1]
    os.remove(notebookToDelete)
    del notebooks[n-1]
    with open('notebooks.txt','w') as f:
        f.write('\n'.join(notebooks))
    print(f'Notebook {notebookToDelete} deleted!\n')

if __name__ == '__main__':
    main()