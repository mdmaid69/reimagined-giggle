def find_unique_words(sentence):
        return set(sentence.split())
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))