import os

def get_txt_files(folder):
    """Return list of all.txt files in folder"""
    files = []
    for name in os.listdir(folder):
        if name.endswith(".txt"):
            files.append(os.path.join(folder, name))
    return files

def read_lines(filepath):
    """Return all lines from a file"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()