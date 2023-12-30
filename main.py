import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)