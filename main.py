import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)