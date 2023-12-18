import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def calculate_volume(length, width, height):
        return length * width * height