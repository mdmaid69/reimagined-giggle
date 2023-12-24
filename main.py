import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)