import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()