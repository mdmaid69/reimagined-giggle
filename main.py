text = "Hello, world!"
print("Uppercase:", text.upper())
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)