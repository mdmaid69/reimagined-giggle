  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))