import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)