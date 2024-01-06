  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import random
def generate_random_number(start, end):
        return random.randint(start, end)