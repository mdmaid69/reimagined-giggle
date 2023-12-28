import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)