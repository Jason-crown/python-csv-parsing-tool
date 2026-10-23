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
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <csv_file.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    data = parse_csv(file_path)
    for row in data:
        print(row)