import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)