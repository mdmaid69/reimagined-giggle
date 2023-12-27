import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)