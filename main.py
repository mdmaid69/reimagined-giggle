import array
def convert_array_to_bytes(array):
        return array.tobytes()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)