import array
def get_array_buffer_info(array):
        return array.buffer_info()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)