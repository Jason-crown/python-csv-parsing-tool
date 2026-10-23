import csv
import sys

def parse_csv(file_path):
    """
    Parses a CSV file and returns its content as a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV rows.
    """
    if not file_exists(file_path):
        return []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def validate_file_path(file_path):
    """
    Validates the provided file path to ensure it is safe and points to a CSV file.

    Args:
        file_path (str): The path to validate.

    Returns:
        bool: True if the file path is valid, False otherwise.
    """
    if not file_path:
        print("Error: File path is empty.")
        return False

    if not file_path.endswith('.csv'):
        print("Error: Only CSV files are allowed.")
        return False

    return True

def filter_invalid_characters(file_path):
    """
    Filters out invalid characters from the file path.

    Args:
        file_path (str): The file path to filter.

    Returns:
        str: The filtered file path."""
    list_of_invalid_chars = ['"', "'", "\\", " ", "..", "~", ":", "*", "?", "<", ">", "|", ";"]
    return ''.join(c for c in file_path if c not in list_of_invalid_chars)

def file_exists(file_path):
    """
    Checks if the specified file exists.

    Args:
        file_path (str): The path to the file.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8'):
            return True
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return False
    
def print_usage():
    """
    Prints the usage instructions for the script.
    """
    print("Usage: python parser.py <csv_file.csv>")

def print_file_content(file_path):
    """
    Prints the content of the specified CSV file.

    Args:
        file_path (str): The path to the CSV file.
    """
    data = parse_csv(file_path)
    for row in data:
        print(row)
        
def print_all_file_content(file_path):
    """
    Prints the content of the specified CSV file, including headers.

    Args:
        file_path (str): The path to the CSV file.
    """
    if not file_exists(file_path):
        return
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def print_file_content_with_headers(file_path):
    """
    Prints the content of the specified CSV file, including headers.

    Args:
        file_path (str): The path to the CSV file.
    """
    if not file_exists(file_path):
        return
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print("Headers:", headers)
        for row in reader:
            print(row)

def print_all_files_content(file_paths):
    """
    Prints the content of multiple CSV files.

    Args:
        file_paths (list): A list of paths to CSV files.
    """
    for file_path in file_paths:
        print(f"Content of {file_path}:")
        print_file_content(file_path)

def print_all_files_content_with_headers(file_paths):
    """
    Prints the content of multiple CSV files, including headers.

    Args:
        file_paths (list): A list of paths to CSV files.
    """
    for file_path in file_paths:
        print(f"Content of {file_path}:")
        print_file_content_with_headers(file_path)
def main() -> int:
    """
    Main function to handle command-line arguments and parse the CSV file."""
    if len(sys.argv) != 2:
        print_usage()
        return 1
    argv = sys.argv[1:]
    file_list = [arg.strip() for arg in argv]
    amount_of_args = len(file_list)
    if amount_of_args != 1:
        print("Error: Please provide exactly one CSV file path.")
        return 1

    file_path = file_list[0]
    valid = validate_file_path(file_path)
    if not valid:
        return 1
    file_path = file_path.strip()
    file_path = filter_invalid_characters(file_path)

    allowed_extensions = ['.csv']
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        print("Error: Only CSV files are allowed.")
        return 1
    
    data = parse_csv(file_path)
    print_file_content(file_path)
    return 0
if __name__ == "__main__":
    sys.exit(main())
