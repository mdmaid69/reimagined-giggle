import random
def generate_random_choice(choices):
        return random.choice(choices)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)