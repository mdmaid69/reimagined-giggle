import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))