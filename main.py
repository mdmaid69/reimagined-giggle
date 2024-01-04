  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)