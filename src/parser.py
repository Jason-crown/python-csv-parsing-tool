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

def main() -> int:
    """
    Main function to handle command-line arguments and parse the CSV file."""
    if len(sys.argv) != 2:
        print("Usage: python parser.py <csv_file.csv>")
        return 1

    file_path = sys.argv[1]
    file_path = file_path.strip()
    list_of_invalid_chars = ['"', "'", "\\", " ", "..", "~", ":", "*", "?", "<", ">", "|", ";"]

    file_path = file_path.replace('"', '').replace("'", "")
    file_path = file_path.replace("\\", "/")  # Normalize path for cross-platform compatibility
    file_path = file_path.replace(" ", "")  # Remove spaces from the path
    file_path = file_path.replace("..", "")  # Prevent directory traversal
    file_path = file_path.replace("~", "")  # Prevent home directory access
    file_path = file_path.replace(":", "")  # Prevent drive access on Windows
    file_path = file_path.replace("*", "")  # Prevent wildcard usage
    file_path = file_path.replace("?", "")  # Prevent wildcard usage
    file_path = file_path.replace("<", "").replace(">", "")  # Prevent redirection
    file_path = file_path.replace("|", "")  # Prevent pipe usage
    file_path = file_path.replace(";", "")  # Prevent command chaining
    allowed_extensions = ['.csv']
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        print("Error: Only CSV files are allowed.")
        return 1
    
    data = parse_csv(file_path)
    for row in data:
        print(row)
    return 0
if __name__ == "__main__":
    sys.exit(main())
