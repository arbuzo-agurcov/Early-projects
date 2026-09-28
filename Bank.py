import time
print('\n\n_____________________________________\n           Console Banking\n         Доступные функции:\n        1. Посмотреть баланс\n      2. Добавить/Убавить баланс\n        3. История банкинга \n_____________________________________\n')
print('Выбирайте, что нам делать!')
total_number = 0 
history = input('')
with open('C:/Users/f7720/Desktop/projects/archive/history.txt', 'a', encoding='utf-8') as file:
    file.write('')
while True:
    choise = input()
    if choise == '1':
            print(f'Сейчас на нашем счету: {total_number}')

    
    if choise == '2':
        target = input('Сколько вы хотите добавить? ')
        try:
            add = int(target)
            total_number += add
            with open('C:/Users/f7720/Desktop/projects/archive/history.txt', 'a', encoding='utf-8') as file:
                file.write(f'{add} рублей было добавлено к счёту! Всего: {total_number}\n')
        except ValueError:
            print('Ошибка. Нужно ввести число')

    elif choise == '3':
        with open('C:/Users/f7720/Desktop/projects/archive/history.txt', 'r', encoding='utf-8') as file:
                        history_content = file.read()
                        print('___________________')
                        print(' История оппераций')
                        print (history_content)
                        print('___________________')

    
    




