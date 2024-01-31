class Cell:
    figure = None
    is_full = False

    def __init__(self, num):
        self.cell_num = num

    def get_num(self):
        return self.cell_num

    def set_status(self, status, player_figure):
        self.is_full = status
        self.figure = player_figure

    def get_status(self):
        return self.is_full

    def get_figure(self):
        return self.figure
