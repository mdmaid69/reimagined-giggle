import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import datetime
def get_today_date():
        return datetime.date.today()