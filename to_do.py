tasks = []

def show_tasks():
    index = 0
    print()
    for task in tasks:
        print(task, index)
        index += 1

def add_task():
    task = input('Podaj zadanie do wykonania: ')
    tasks.append(task)
    
def delete_task():
    deleted = int(input('Które zadanie chcesz usunąć? '))
    try:
        tasks.pop(deleted)
    except IndexError:
        print('Nie ma zadania o takim numerze!')
    return

def save_to_file():
    with open('tasks.txt', 'a') as file:
        for task in tasks:
            file.write(str(task + '\n'))
       
    
def read_from_file():
    with open('tasks.txt', 'r') as file:
        list_of_tasks = file.readlines()
        print('Aktualna lista zadań:')
        for _ in list_of_tasks:
            print(_)
        

        
 
while True:
    
    print()
    print('1. Pokaż aktualne zadania.')
    print('2. Dodaj zadanie.')
    print('3. Usuń zadanie.')
    print('4. Zapisz zmiany.')
    print('5. Odczytaj dane z pliku.')
    print('6. Wyjdź z programu.')
    
    choice = int(input('Co chcesz zrobić? '))
    
    if choice not in (1,2,3,4,5,6):
        print('To nie jest poprawne polecenie dla programu! Wybierz ponownie.\n')
    else:
        if choice == 1:
            show_tasks()
        if choice == 2:
            add_task()
        if choice == 3:
            delete_task()
        if choice == 4:
            save_to_file()
        if choice == 5:
            read_from_file()
        if choice == 6:
            print('Lista zadań zamknięta.')
            break
            
    
    
            


    
    