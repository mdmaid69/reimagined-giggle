import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)