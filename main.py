import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))