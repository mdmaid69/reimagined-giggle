import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)