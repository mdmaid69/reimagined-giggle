import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)