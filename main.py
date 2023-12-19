import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_volume(length, width, height):
        return length * width * height