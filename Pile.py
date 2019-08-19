""" Represents a sandpile and it's various states as grains of sand are added """

import collections
from Step import Step

class Pile:

    def __init__(self, size):
        self.size = size
        self.steps = []

        # set first step IC to all zeros
        cols = []
        for i in range(size):
            cols.append([])
            for j in range(size):
                cols[i].append(0)

        init_step = Step(self.size)
        init_step.set_init_cond(cols)
        self.steps.append(init_step)

    def add_grain(self, x_pos, y_pos):
        next_step = self.steps[-1].add_grain(x_pos, y_pos)
        self.steps.append(next_step)

    def get_freq_dist(self):
        freq_dict = dict()
        for step in self.steps:
            key = step.avalanche_size
            if key == 0:
                continue
            value = freq_dict.get(key, 0)
            value = value + 1
            freq_dict[key] = value

        ord_freq_dict = collections.OrderedDict(sorted(freq_dict.items()))
        return ord_freq_dict

    def get_num_states(self):
        states = 0
        for step in self.steps:
            states = states + len(step.states)
        return states

    def get_num_steps(self):
        return len(self.steps)

    def set_init_cond(self, cols):
        self.steps.clear()
        new_step = Step(self.size)
        new_step.set_init_cond(cols)
        self.steps.append(new_step)
        return



    def __str__(self):
        string = ''
        for idx, step in enumerate(self.steps):
            if idx == 0:
                string = string + 'Initial Condition:\n'
            else:
                string = string + 'Step {}:\n'.format(idx)
            string = string + str(step) + '\n'
        return string

