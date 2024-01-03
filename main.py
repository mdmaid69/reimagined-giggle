import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import sqlite3
  def close_database_connection(connection):
        connection.close()