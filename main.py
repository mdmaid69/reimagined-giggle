import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def delete_file(file_name):
        os.remove(file_name)