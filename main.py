def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)