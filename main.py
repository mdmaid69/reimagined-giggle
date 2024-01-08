import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)