from all_file_readers.text_reader import TextReader


def main():
    the_reader = TextReader(r"C:\Users\USER\Documents\random_csv_file.csv")
    TextReader.read(the_reader)


if __name__ == '__main__':
    main()

