  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()