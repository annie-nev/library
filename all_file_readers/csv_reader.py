import csv

from file_reader import FileReader
from utils.string_utils import slice_words


class CsvReader(FileReader):

    def read(self, max_char_count: int = 5):
        all_rows_list = []
        with open(self.file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sliced_row = slice_words(row, max_char_count)
                to_print = self.print_row_table(sliced_row)
                print(to_print)



    def print_row_table(self, sliced_row : list[str]):
        final_word_format = []
        for sliced_word in sliced_row:
            final_str = "|" + sliced_word + " "*(5-len(sliced_word)) + "|"
            final_word_format.append(final_str)
        return "".join(final_word_format)

    # TODO: bugfix - replace 5 with self.max_char_count



