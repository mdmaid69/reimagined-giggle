import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)