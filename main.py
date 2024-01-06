  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)