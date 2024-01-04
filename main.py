  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))