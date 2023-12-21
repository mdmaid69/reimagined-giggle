import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)