import csv

from file_reader import FileReader
from utils.stringutils import slice_words


class CsvReader(FileReader):

    def read(self, max_char_count: int = 5):
        with open(self.file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sliced_row = slice_words(row, max_char_count)
                print(sliced_row)


