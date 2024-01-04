n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)