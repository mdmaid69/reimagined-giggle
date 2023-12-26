import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)