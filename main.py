  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")