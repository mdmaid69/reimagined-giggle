import shutil
def delete_directory(path):
        shutil.rmtree(path)
def remove_duplicates(lst):
        return list(set(lst))