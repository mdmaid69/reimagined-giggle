  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")