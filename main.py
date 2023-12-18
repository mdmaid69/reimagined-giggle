  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))