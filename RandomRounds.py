""" This model represents a basic sandpile simulation with rounds of random grain placement """

import random
from Pile import Pile

if __name__ == '__main__':
    pile = Pile(5)

    for i in range(1000):
        x_pos = random.randint(0, 4)
        y_pos = random.randint(0, 4)
        pile.add_grain(x_pos, y_pos)

    print(pile)
    print(pile.get_freq_dist())
    print('Done')
