numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)