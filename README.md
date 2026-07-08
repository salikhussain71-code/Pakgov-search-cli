# PakGov Document Search CLI

A command-line tool built in Python to search keywords across multiple Pakistani government text documents. This was my CS50P Final Project.

## Problem
Government employees, researchers, and students often need to find specific information across hundreds of text files and PDFs. Doing this manually is slow and error-prone.

## Solution
PakGov Search CLI scans all `.txt` files inside a `docs/` folder, finds exact keyword matches, and shows 1 line of context before and after each match. Every search is automatically logged to a CSV file with a timestamp for record keeping.

## Features
- **Fast Keyword Search**: Search across multiple `.txt` files instantly
- **Context Display**: Shows 1 line before and after each match for better understanding
- **Search History**: All searches saved to `history.csv` with date and time
- **Error Handling**: Custom exceptions for empty queries and missing folders
- **Modular Code**: Clean separation using `document_reader.py` and `exceptions.py`

## Technologies Used
- **Language**: Python 3
- **Libraries**: `os`, `csv`, `re`, `datetime`, `sys`
- **Concepts**: File I/O, Regular Expressions, Custom Exceptions, CLI

## How to Run
1. Clone the repository
   ```bash
   git clone https://github.com/salikhussain71-code/Pakgov-search-cli.git
   cd Pakgov-search-cli
