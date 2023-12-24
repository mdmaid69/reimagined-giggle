  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))