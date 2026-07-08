import os

def get_txt_files(folder):
    """Return list of all .txt files in folder"""
    txt_files = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            txt_files.append(os.path.join(folder, filename))
    return txt_files


def read_lines(filepath):
    """Read file and return list of lines"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.readlines()
    except:
        return []
