import datetime
def get_current_datetime():
        return datetime.datetime.now()
import shutil
def delete_directory(path):
        shutil.rmtree(path)