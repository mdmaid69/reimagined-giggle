  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)