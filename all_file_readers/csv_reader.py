import csv

from file_reader import FileReader
from utils.string_utils import slice_words


class CsvReader(FileReader):

    def read(self, max_char_count: int = 5):
        with open(self.file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sliced_row = slice_words(row, max_char_count)
                to_print = self.print_row_table(sliced_row, max_char_count)
                print(to_print)

    @staticmethod
    def print_row_table(sliced_row: list[str], max_char_count):
        final_word_format = []
        for sliced_word in sliced_row:
            final_str = "|" + sliced_word + " "*(max_char_count-len(sliced_word)) + "|"
            final_word_format.append(final_str)
        return "".join(final_word_format)



