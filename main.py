  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))