import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)