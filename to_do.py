


def show_tasks():
    index = 0
    print()
    print('Aktualna lista zadań:\n')

    for task in tasks:
        print(f"[{index}] {task}")
        index += 1

def add_task():
    task = input('Podaj zadanie do wykonania: ')
    tasks.append(task)
    print('Zadanie zostało dopisane.')
    
def delete_task():
    deleted = input('Które zadanie chcesz usunąć? (PODAJ JEGO NUMER) ')
    
    try:
        deleted = int(deleted)
        tasks.pop(deleted)
        print('Zadanie zostało usunięte.')
    except ValueError:
        print('Niepoprawny numer zadania!')
    except IndexError:
        print('Nie ma zadania o takim numerze!')

def save_to_file():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
       
    
def read_from_file():
    global tasks
    
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        print('Zadania zostały załadowane z pliku.')

    except FileNotFoundError:
        tasks = []
        

read_from_file()
while True:
    
    print()
    print('1. Pokaż aktualne zadania.')
    print('2. Dodaj zadanie.')
    print('3. Usuń zadanie.')
    print('4. Zapisz zmiany.')
    print('5. Wyjdź z programu.')
    print()
    choice = input('Co chcesz zrobić? ')
    print()
    
    
    if choice not in ('1','2','3','4','5'):
        print('To nie jest poprawne polecenie dla programu! Wybierz ponownie.\n')
    else:
        if choice == '1':
            show_tasks()
        if choice == '2':
            add_task()
        if choice == '3':
            delete_task()
        if choice == '4':
            save_to_file()
        if choice == '5':
            print('Lista zadań zamknięta.')
            break
