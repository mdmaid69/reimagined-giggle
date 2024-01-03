  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()