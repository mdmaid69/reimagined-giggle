import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)