  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import logging
def log_message(message):
        logging.info(message)