import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)