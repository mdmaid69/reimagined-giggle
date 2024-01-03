  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def find_unique_words(sentence):
        return set(sentence.split())