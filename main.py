import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)