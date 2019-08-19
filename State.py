""" Represents a single state in a simulation """

import copy

class State:

    def __init__(self, cols):
        self.columns = cols.copy()

    def add_grain(self, x_pos, y_pos):
        new_cols = copy.deepcopy(self.columns)
        try:
            new_cols[x_pos][y_pos] = new_cols[x_pos][y_pos] + 1
        except IndexError:
            # Let the grain "fall off" if it's OOB
            pass
        return State(new_cols)

    def __str__(self):
        string = str(self.columns)
        string = string.replace('],', '],\n')
        string = string + '\n'
        return string
