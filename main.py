  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)