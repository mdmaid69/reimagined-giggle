  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"