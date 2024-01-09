  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))