import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))