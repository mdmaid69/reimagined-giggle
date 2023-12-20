  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)