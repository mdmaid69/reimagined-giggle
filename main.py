import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()