  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)