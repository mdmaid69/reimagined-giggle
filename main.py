import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)