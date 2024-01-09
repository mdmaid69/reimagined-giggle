def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list