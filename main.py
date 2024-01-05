import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)