import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)