  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))