import os
import json
import csv

def count_file_content(file_path):
    try:
        extension = os.path.splitext(file_path)[1].lower()

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            characters = len(content)

        print(f"\nFile: {file_path}")
        print(f"Extension: {extension}")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"⚠️ Error reading file {file_path}: {e}")

def summary_for_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            lines = len(rows)
            words = sum(len(row) for row in rows)
            characters = sum(len(str(cell)) for row in rows for cell in row)

        print(f"\nFile: {file_path}")
        print("Extension: .csv")
        print(f"Lines (rows): {lines}")
        print(f"Words (cells): {words}")
        print(f"Characters: {characters}")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"⚠️ Error reading CSV file: {e}")

def summary_for_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            content = json.dumps(data, indent=2)
            lines = content.count('\n') + 1
            words = len(content.split())
            characters = len(content)

        print(f"\nFile: {file_path}")
        print("Extension: .json")
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {characters}")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"⚠️ Error decoding JSON file: {file_path}")
    except Exception as e:
        print(f"⚠️ Error reading JSON file: {e}")

def generate_summary(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == '.txt':
        count_file_content(file_path)
    elif extension == '.csv':
        summary_for_csv(file_path)
    elif extension == '.json':
        summary_for_json(file_path)
    else:
        print(f"❌ Unsupported file type: {extension}")

if __name__ == "__main__":
    files_to_check = [
        "sample.txt",
        "data.csv",
        "info.json"
    ]

    for file in files_to_check:
        generate_summary(file)
