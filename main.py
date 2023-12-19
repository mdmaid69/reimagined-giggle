  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value