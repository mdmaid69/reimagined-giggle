  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)