# PakGov Document Keyword Search CLI

**CS50P Final Project by Salik**
**Start: July 2026 | End: August 2026**

## What is this?
A command-line tool to search Pakistani government document extracts.
User enters a keyword. Tool scans all.txt files in `docs/` and returns
filename, line number, and context.

This is the seed project for my larger PAKGOV-RAG bilingual NLP system.

## Features
- Search by keyword in multiple.txt files
- Shows 1 line before and after for context
- Case insensitive search using regex
- Saves search history to CSV with timestamp
- Custom exceptions for empty input and missing folder

## How to Run
1. Put your.txt files inside the `docs/` folder
2. Open terminal in this folder
3. Run: `python search.py`
4. Enter your keyword when asked

## Files
| File | Purpose |
|------|---------|
| `search.py` | Main program and search logic |
| `document_reader.py` | Reads files from docs folder |
| `exceptions.py` | Custom error handling |
| `history.csv` | Logs all searches |
| `docs/` | Folder for your documents |

## What I Learned
File I/O, functions, modules, exceptions, CSV, regex, and CLI design.

Built for CS50P Harvard.