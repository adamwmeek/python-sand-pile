""" Defines how columns end up in topple condition and how this effects the state """

import copy

class BasicToppleRule:

    def will_topple(self, cols, x_pos, y_pos):
        """ In this example, a column will topple if height > 4 """
        height = cols[x_pos][y_pos]
        return height >= 4

    def has_topples(self, cols, size):

        for i in range(size):
            for j in range(size):
                if self.will_topple(cols, i, j):
                    return True

        return False

    def num_topples(self, cols, size):

        num = 0
        for i in range(size):
            for j in range(size):
                if self.will_topple(cols, i, j):
                    num = num + 1

        return num

    def topple_cols(self, cols, size):

        new_cols = copy.deepcopy(cols)

        for i in range(size):
            for j in range(size):
                if self.will_topple(cols, i, j):
                    new_cols[i][j] = 0

                    for k in range(-1, 2):

                        neighbor_x = i + k
                        list_range = [0]

                        if k == 0:
                            list_range = [-1, 1]

                        for l in list_range:

                            neighbor_y = j + l

                            if neighbor_x >= size or neighbor_x < 0:
                                # Don't move this grain OOB or back onto the start
                                continue

                            if neighbor_y >= size or neighbor_y < 0:
                                continue

                            new_cols[neighbor_x][neighbor_y] = new_cols[neighbor_x][neighbor_y] + 1

        return new_cols

