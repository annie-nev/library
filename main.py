from all_file_readers.csv_reader import CsvReader


def main():
    the_reader = CsvReader(r"C:\Users\USER\Documents\random_dir\random_csv_file.csv")
    CsvReader.read(the_reader)


if __name__ == '__main__':
    main()

