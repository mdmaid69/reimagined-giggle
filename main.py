import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b