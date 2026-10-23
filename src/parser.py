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



def main() -> int:
    """
    Main function to handle command-line arguments and parse the CSV file."""
    if len(sys.argv) != 2:
        print("Usage: python parser.py <csv_file.csv>")
        return 1

    file_path = sys.argv[1]
    data = parse_csv(file_path)
    for row in data:
        print(row)
    return 0
if __name__ == "__main__":
    sys.exit(main())
