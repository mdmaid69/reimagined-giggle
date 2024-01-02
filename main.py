  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))