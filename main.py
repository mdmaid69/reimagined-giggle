import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])