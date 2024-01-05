import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import datetime
def get_today_date():
        return datetime.date.today()