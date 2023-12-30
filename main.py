import collections
def create_user_list():
        return collections.UserList()
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))