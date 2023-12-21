  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())