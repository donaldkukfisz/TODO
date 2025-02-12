# LISTA TO DO Z OPCJÄ„ DODAWANIA I ODEJMOWANIA RZECZY

#Potrzeba:
# opcja dodania rzeczy do chcecklisty
# opcja wyswietlenia statusu czy rzecz jest wykonana klucz-wartoc
# opcja usuwania rzeczy

import json
import time


#  wczytanie listy zadan
try:
    with open('to_do_list.json','r') as file:
        to_do_list = json.load(file)
except FileNotFoundError:
    to_do_list = {}

# drukowanie aktualnej listy zadań z zapisanego pliku
print("Aktualna lista zadań:") 
for key, value in to_do_list.items():
    print(f"{key}, status: {value}")


# pierwsza pętla dodająca zadania
while True:
    print('')
    task = input('Co jest do zrobienia? ').strip()
    
    if not task:
        print('Nie można dodać pustego zadania!')
        continue
    to_do_list[task] = 'niewykonane'
    
    if task in to_do_list:
        print(f"Zadanie '{task}' zostało już wczesniej dodane!")
        continue
    
    print('')
    question = input('Czy chcesz dodać kolejne zadania? T/N? ')
    if question.lower() != 't':
        break
    
  


# drukowanie zaktualizowanej listy zadań
print('')
print("Aktualizacja zadań:")
for key, value in to_do_list.items():
    print(f"{key}, status: {value}")

time.sleep(2)

# zapisywanie listy zadań znóW do pliku
with open('to_do_list.json', 'w') as file:
    json.dump(to_do_list, file)



