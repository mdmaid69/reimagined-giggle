  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))