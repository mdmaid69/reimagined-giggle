def count_words(sentence):
        return len(sentence.split())
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))