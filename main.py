import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)