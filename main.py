import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)