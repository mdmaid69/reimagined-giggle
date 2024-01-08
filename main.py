  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))