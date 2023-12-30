import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)