import sklearn.datasets
print(sklearn.datasets.load_iris())
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)