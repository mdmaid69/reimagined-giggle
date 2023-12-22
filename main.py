def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)