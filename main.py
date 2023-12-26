  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))