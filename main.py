  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)