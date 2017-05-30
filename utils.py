import os

def create_dir_if_needed(path):
    if not os.path.isdir(path):
        os.makedirs(path)
