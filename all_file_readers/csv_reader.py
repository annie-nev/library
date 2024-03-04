import csv

from file_reader import FileReader


class CsvReader(FileReader):

    def slice_words(self, word_list: list[str]):
        sliced_word_list = []
        for word in word_list:
            new_word = word[:5]
            sliced_word_list.append(new_word)
        return sliced_word_list

    def read(self, max_char_count: int = 5):
        with open(self.file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sliced_row = self.slice_words(row)
                print(sliced_row)


