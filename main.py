  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import logging
def log_message(message):
        logging.info(message)