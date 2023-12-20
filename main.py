import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))