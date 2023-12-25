  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)