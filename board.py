from cell import Cell


class Board:
    board = None

    def create_board(self):
        self.board = [
            [Cell(num) for num in range(1, 4)],
            [Cell(num) for num in range(4, 7)],
            [Cell(num) for num in range(7, 10)]
        ]

    def get_board(self):
        return self.board

    def check_tie(self):
        cell_status = [cell.get_status() for line in self.board for cell in line]
        return all(cell_status)

    def check_win(self, player_figure):
        solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        figure_list = [
            cell.get_figure()
            for line in self.board
            for cell in line
        ]

        for combination in solution:
            check_list = [figure_list[num - 1] for num in combination]
            if check_list.count(player_figure) == 3:
                return True
        else:
            return False

    def print_board(self):
        print('------------')
        for line in self.board:
            for cell in line:
                if cell.get_status():
                    print(' {} '.format(cell.get_figure()), end='|')
                else:
                    print(' {} '.format(cell.get_num()), end='|')
            print()
            print('------------')
