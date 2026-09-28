import time

Risovashka = {
    "Камень": "Бумага",
    "Ножницы": "Камень",
    "Бумага": "Ножницы"
}

def play_a_game(): 
    print('Камень, ножницы бумага. Сыграем?')
    print('Просто введи свой вариант')
    
    # Исправили: пробел после while, двоеточие в конце строки
    while True:
        # Добавили .strip().capitalize(), чтобы код понимал ввод "камень" с маленькой буквы
        choise = input('Выберите рисовашку (Камень, Ножницы, Бумага): ').strip().capitalize()
        
        if choise not in Risovashka:
            print('Что ты высрал')
            continue # Возвращает в начало цикла для повторного ввода
            
        print('Рисовашкин думает..')
        time.sleep(1)
        
        ai_choise = Risovashka[choise]
        
        print(f'Вы выбрали: {choise}')
        print(f'Компьютер выбрал {ai_choise}')
        print('Вы проиграли, красавчик\n')
play_a_game()