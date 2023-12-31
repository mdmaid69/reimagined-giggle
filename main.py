import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)