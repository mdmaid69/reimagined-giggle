import random
def roll_die():
        return random.randint(1, 6)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)