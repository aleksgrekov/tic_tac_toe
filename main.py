from game import Game

game = Game()
print('*** КРЕСТИКИ - НОЛИКИ ***')
while True:
    print('\nСыграем?\n1 - "Да"\n2 - "Нет"')
    try:
        shall_we_play = int(input('Введите число: '))
        if shall_we_play == 1:
            game.start_tic_tac_toe()
        elif shall_we_play == 2:
            print('До свидания!')
            break
        else:
            raise ValueError
    except ValueError:
        print('Ошибка ввода! попробуйте ещё раз!')
