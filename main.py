import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)