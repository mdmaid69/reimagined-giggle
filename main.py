import sklearn.datasets
print(sklearn.datasets.load_iris())
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)