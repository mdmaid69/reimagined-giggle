import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import datetime
def get_today_date():
        return datetime.date.today()