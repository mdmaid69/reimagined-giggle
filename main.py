def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)