  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))