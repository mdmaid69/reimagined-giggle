  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5