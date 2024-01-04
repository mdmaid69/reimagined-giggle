import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)