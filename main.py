def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list