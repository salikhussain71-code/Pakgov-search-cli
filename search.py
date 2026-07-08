import os
import sys
import csv
import re
from datetime import datetime
from document_reader import get_txt_files, read_lines
from exceptions import EmptyQueryError, FolderNotFoundError

DOCS_FOLDER = "docs"
HISTORY_FILE = "history.csv"

def main():
    print("=== PakGov Document Search CLI ===")

    # Check if docs folder exists
    if not os.path.exists(DOCS_FOLDER):
        raise FolderNotFoundError(f"Folder '{DOCS_FOLDER}' not found")

    # Get keyword from user
    keyword = input("Enter keyword to search: ").strip()

    if keyword == "":
        raise EmptyQueryError("Query cannot be empty")

    # Search
    results = search_keyword(keyword)

    # Show results
    if len(results) == 0:
        print("No matches found.")
    else:
        for r in results:
            print(f"\nFile: {r['file']} | Line: {r['line_num']}")
            print(f"...{r['before']}")
            print(f">>> {r['match']}")
            print(f"...{r['after']}")

    # Save to history
    save_history(keyword, len(results))

def search_keyword(keyword):
    """Search keyword in all txt files"""
    results = []
    files = get_txt_files(DOCS_FOLDER)

    for file in files:
        lines = read_lines(file)
        for i in range(len(lines)):
            # case insensitive search
            if re.search(keyword, lines[i], re.IGNORECASE):
                before = lines[i-1].strip() if i > 0 else ""
                after = lines[i+1].strip() if i < len(lines)-1 else ""
                results.append({
                    "file": file,
                    "line_num": i + 1,
                    "before": before,
                    "match": lines[i].strip(),
                    "after": after
                })
    return results

def save_history(keyword, count):
    """Save search to CSV"""
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # write header only if file is new
        if f.tell() == 0:
            writer.writerow(["timestamp", "keyword", "results_count"])
        writer.writerow([datetime.now(), keyword, count])

if __name__ == "__main__":
    try:
        main()
    except EmptyQueryError as e:
        print(f"Error: {e}")
    except FolderNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")