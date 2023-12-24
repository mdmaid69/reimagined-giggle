list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)