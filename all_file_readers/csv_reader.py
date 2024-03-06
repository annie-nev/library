"""
Purpose: Implements CsvReader class
Author: Annie_nev
Created:5.3.2024
"""

import csv
from file_reader import FileReader
from utils.string_utils import slice_words


class CsvReader(FileReader):
    """
     Implements CsvReader functions
    """
    def read(self, max_char_count: int = 5):
        """
        prints csv files in table format
        :param max_char_count: character limit for each cell
        """
        with open(self.file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sliced_row = slice_words(row, max_char_count)
                to_print = self.print_row_table(sliced_row, max_char_count)
                print(to_print)
        return

    @staticmethod
    def print_row_table(sliced_row: list[str], max_char_count: int):
        """
        changes each row to be in
        the correct format for printing
        :param sliced_row: a list of all words in one row according to max_char_count
        :param max_char_count: character limit for each cell
        :return: 1 row as string for printing
        """
        final_word_format = []
        for sliced_word in sliced_row:
            final_str = "|" + sliced_word + " "*(max_char_count-len(sliced_word)) + "|"
            final_word_format.append(final_str)
        return "".join(final_word_format)



