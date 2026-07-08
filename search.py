import os
import sys
import csv
import re
from datetime import datetime
from document_reader import get_txt_files, read_lines
from exceptions import EmptyQueryError, FolderNotFoundError

DOCS_FOLDER = "docs"
HISTORY_FILE = "history.csv"


def save_to_history(keyword, results_count):
    """Save each search to history.csv with timestamp"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(HISTORY_FILE)
    
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "keyword", "results_found"])
        writer.writerow([now, keyword, results_count])


def search_in_file(filepath, keyword):
    """Search keyword in one file and return matches with context"""
    lines = read_lines(filepath)
    matches = []
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    
    for i, line in enumerate(lines):
        if pattern.search(line):
            # get 1 line before and after for context
            before = lines[i-1].strip() if i > 0 else ""
            after = lines[i+1].strip() if i < len(lines) - 1 else ""
            matches.append({
                "line_num": i + 1,
                "match": line.strip(),
                "before": before,
                "after": after
            })
    return matches


def main():
    print("=== PakGov Document Search CLI ===")
    print()

    # Check if docs folder exists
    if not os.path.exists(DOCS_FOLDER):
        raise FolderNotFoundError(f"Folder '{DOCS_FOLDER}' not found. Please create a 'docs' folder.")

    # Get keyword from user
    keyword = input("Enter keyword to search: ").strip()
    
    if keyword == "":
        raise EmptyQueryError("Keyword cannot be empty.")

    print(f"\nSearching for '{keyword}' in {DOCS_FOLDER}...\n")

    txt_files = get_txt_files(DOCS_FOLDER)
    total_matches = 0

    if not txt_files:
        print("No .txt files found in docs folder.")
        return

    for filepath in txt_files:
        filename = os.path.basename(filepath)
        results = search_in_file(filepath, keyword)
        
        if results:
            print(f"--- Found in: {filename} ---")
            for r in results:
                total_matches += 1
                print(f"Line {r['line_num']}: {r['match']}")
                if r['before']:
                    print(f"  Context: ...{r['before']}")
                if r['after']:
                    print(f"           {r['after']}...")
            print()

    # Save to history
    save_to_history(keyword, total_matches)

    if total_matches == 0:
        print(f"No matches found for '{keyword}'.")
    else:
        print(f"Total matches found: {total_matches}")
        print(f"Search saved to {HISTORY_FILE}")


if __name__ == "__main__":
    try:
        main()
    except FolderNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except EmptyQueryError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
