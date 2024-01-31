class Player:
    score = 0

    def __init__(self, name, figure):
        self.player_name = name
        self.figure = figure

    def move_to_cell(self):
        try:
            cell_num = int(input('Введите номер клетки (От 1 до 9): '))
            if 0 < cell_num <= 9:
                return cell_num
            else:
                raise ValueError
        except ValueError:
            print('Клетки с таким числом не существует!')
            return self.move_to_cell()

    def get_name(self):
        return self.player_name

    def get_figure(self):
        return self.figure

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score
