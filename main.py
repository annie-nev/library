from all_file_readers.csv_reader import CsvReader
from all_file_readers.json_reader import JsonReader


def main():
    the_reader = JsonReader(r"C:\Users\USER\Documents\random_json_file.json")
    JsonReader.read(the_reader)


if __name__ == '__main__':
    main()

