  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list