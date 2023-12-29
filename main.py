import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)