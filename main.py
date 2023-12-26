  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)