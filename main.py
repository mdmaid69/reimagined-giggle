import math
def calculate_permutations(n, k):
        return math.perm(n, k)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)