  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))