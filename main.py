  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))