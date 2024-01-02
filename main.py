import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def calculate_energy(mass, c=3*10**8):
        return mass * c**2