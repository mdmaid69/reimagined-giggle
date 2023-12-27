n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)