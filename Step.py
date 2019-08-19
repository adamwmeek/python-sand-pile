""" Represents a single step in manipulating a sandpile
    A single step can result in multiple different states, as avalanches can occur
"""
import copy

from State import State
from ToppleRules.BasicToppleRule import BasicToppleRule

class Step:

    def __init__(self, size):
        #TODO: IoC for topple rules
        self.size = size
        self.avalanche_size = 0
        self.states = []
        self.tr = BasicToppleRule()

    def add_grain(self, x_pos, y_pos):
        start_state = self.states[-1]
        new_step = Step(self.size)
        next_state = start_state.add_grain(x_pos, y_pos)
        new_step.states.append(next_state)
        while self.tr.has_topples(next_state.columns, self.size):
            new_step.avalanche_size = new_step.avalanche_size + self.tr.num_topples(next_state.columns, self.size)
            new_cols = self.tr.topple_cols(next_state.columns, self.size)
            next_state = State(new_cols)
            new_step.states.append(next_state)
        return new_step

    def set_init_cond(self, cols):
        self.states.clear()
        self.avalanche_size = 0
        self.states.append(State(cols))

    def __str__(self):
        string = ''
        #TODO: how to format this to fit to console width
        for state in self.states:
            string = string + str(state) + '\n'
        string = string + '\nAvalanche size: {}\n'.format(self.avalanche_size)
        return string

