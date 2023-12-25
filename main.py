import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)