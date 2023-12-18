import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))