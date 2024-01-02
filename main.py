import shutil
def delete_directory(path):
        shutil.rmtree(path)
text = "Hello, world!"
print("Words:", len(text.split()))