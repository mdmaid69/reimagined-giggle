import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5