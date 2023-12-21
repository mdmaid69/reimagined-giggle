text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)