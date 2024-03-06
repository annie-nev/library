import os

from all_file_readers.csv_reader import CsvReader
from all_file_readers.text_reader import TextReader
# from all_file_readers.json_reader import JsonReader
from file_reader import FileReader


def dir_walk(path):
    object_list = []
    for filename in os.listdir(path):
        # file_path = FileReader(filename)
        # file_type = (FileReader.name(file_path)).split(".")[-1]
        file_type = (filename.split("."))[-1]
        if file_type == "txt":
            text_object = TextReader(path+ "\\" +filename)
            object_list.append(text_object)
        elif file_type == "csv":
            csv_object = CsvReader(path+ "\\" +filename)
            object_list.append(csv_object)
        # elif file_type == "json":
        #     json_object = JsonReader(filename)
        #     object_list.append(json_object)
        else:
            pass



    def read(self):
        pass

