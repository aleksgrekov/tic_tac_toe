from board import Board
from player import Player


class Game:
    players = list()
    board = Board()

    def add_players(self):
        player1_name = input('\nВведите имя игрока для фигуры "X": ')
        player2_name = input('Введите имя игрока для фигуры "O": ')
        self.players.append(Player(player1_name, 'X'))
        self.players.append(Player(player2_name, 'O'))

    def start_progress(self, player):
        if self.board.check_tie():
            print('Ничья! Все клетки уже заняты!')
            return True

        move = player.move_to_cell()
        for line in self.board.get_board():
            for cell in line:
                if cell.get_num() == move:
                    if not cell.get_status():
                        print('Игрок {name} поставил {figure} на клетку {num}'.format(
                            name=player.get_name(),
                            figure=player.get_figure(),
                            num=move
                        ))
                        cell.set_status(True, player.get_figure())
                        is_win = self.board.check_win(player.get_figure())
                        if is_win:
                            print('ИГРОК {} ОДЕРЖАЛ ПОБЕДУ!!!\n'.format(player.get_name().upper()))
                            player.set_score(player.get_score() + 1)
                            return True
                        else:
                            return False
                    else:
                        print('Эта клетка уже занята! Выберете другую.')
                        return self.start_progress(player)

    def start_one_game(self):
        self.board.create_board()

        player_move = False
        while not player_move:
            for player in self.players:
                print('\nХод игрока {}'.format(player.get_name()))
                self.board.print_board()
                player_move = self.start_progress(player)
                if player_move:
                    return True
        else:
            return False

    def start_tic_tac_toe(self):
        self.add_players()
        game_count = 1
        while True:
            print('\nИгра №{}'.format(game_count))
            self.start_one_game()
            for player in self.players:
                print('Счёт игрока {name}: {score}'.format(
                    name=player.get_name(),
                    score=player.get_score()
                ))

            game_count += 1

            print('Ещё разок?\n1 - Да\n2 - Нет')
            try:
                answer = int(input('Введите число: '))
                if answer == 1:
                    continue
                elif answer == 2:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Ошибка ввода! попробуйте ещё раз!')
