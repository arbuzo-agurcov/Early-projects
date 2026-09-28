import time

Gaika = ['Добавить','Удалить','Редактировать', 'Узнать']
text = 'Пока что здесь ничего нет'
Redakt = ['Текст', 'Ничего']
Udalyator = ['Текст', 'Себя']
print('Что сделаем с нашим список\n Добавим?(Добавить) | Удалим?(Удалить) | Редактируем(Редактировать) | Узнать текст (Узнать)')
    

while True:
    choise = input('Выбирай! ')
    if choise not in Gaika:
        print('Ещё раз, не понял.')
        continue

    print('Заносим..')
    time.sleep(1)

    
    if choise == 'Редактировать':
        redaktor = input('Что именно ты собираешься редактировать?(Текст)  ')
        
        if redaktor not in Redakt:
            print('Я такого не знаю')
        elif redaktor == 'Текст':
            print('Я не шарю, как это делается, в разработке ')

    
    elif choise == 'Удалить':
        udal = input('Что именно удалить? (Текст | Себя) ')
        
        if udal not in Udalyator:
            print('Ничего не понял')
        elif udal == 'Себя':
            break
        elif udal == 'Текст':
            text = ''
            print('Окей, text удалён!')

    elif choise == 'Добавить':
        add = input('Что именно нужно добавить? (Текст | Ничего)  ')
        if add not in Redakt:
            print('Я тебя не понимаю.')
        elif add == 'Текст':
            text = input('Что вы хотите ввести?')
            print(f'Хорошо, текст был добавлен! Ваш текст:\n {text}')
        elif add == 'Ничего':
            print('Ну, ладно.')
            continue

    elif choise == 'Узнать':
        if text == '':
            print('Сейчас в нашем тексте ничего нет')
        else:
            print(f'Актуальный текст:\n{text}')
    




        



