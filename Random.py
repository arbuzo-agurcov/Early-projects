import random

minimal = 50
maximum = 80
print('Игра: угадай число')
while True:
    Randomchik = random.randint(50,80)
    choise = int(input(f'Введи число от {minimal} до {maximum} '))
    if choise < minimal or choise > maximum:
            print('Прочитай внимательно, что от тебя просят!')
    elif choise == Randomchik:
         print(f'Ты угадал. Число было: {Randomchik}')
         continue
    elif choise <= Randomchik -5:
        print(f'Холодно, число было {Randomchik}')
    elif choise <= Randomchik +5:
        print(f'Ни жарко ни холодно, число было {Randomchik}')
    elif choise <= Randomchik +20:
        print(f'Холодно, число было {Randomchik}')
    

