import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def calculate_roi(gain, cost):
        return (gain - cost) / cost