import datetime
def get_current_date():
        return datetime.date.today()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)