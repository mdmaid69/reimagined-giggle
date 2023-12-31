import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list