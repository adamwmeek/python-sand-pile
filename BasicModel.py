""" This model represents a basic sandpile simulation, as described by Bak """

from Pile import Pile


if __name__ == '__main__':
    pile = Pile(5)

    # Given pile ICs
    cols = [[1, 2, 0, 2, 3],
            [2, 3, 2, 3, 0],
            [1, 2, 3, 3, 2],
            [3, 1, 3, 2, 1],
            [0, 2, 2, 1, 2]]

    pile.set_init_cond(cols)
    pile.add_grain(2, 2)
    print(pile)
    print(pile.get_freq_dist())
    print('Done')
