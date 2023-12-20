import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)