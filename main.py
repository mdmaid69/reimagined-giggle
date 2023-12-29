  import sqlite3
  def close_database_connection(connection):
        connection.close()
import sklearn.datasets
print(sklearn.datasets.load_iris())