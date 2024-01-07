  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
text = "Hello, world!"
print("Words:", len(text.split()))