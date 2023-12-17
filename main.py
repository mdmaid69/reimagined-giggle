import datetime
print(datetime.datetime.now())
import shutil
def delete_directory(path):
        shutil.rmtree(path)