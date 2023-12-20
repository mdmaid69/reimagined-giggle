  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list