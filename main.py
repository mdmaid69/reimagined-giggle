def calculate_circumference_circle(r):
        return 2 * 3.14 * r
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)