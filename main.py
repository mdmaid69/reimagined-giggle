  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))