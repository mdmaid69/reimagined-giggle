import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)