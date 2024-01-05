import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)