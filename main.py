  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import datetime
def get_today_date():
        return datetime.date.today()