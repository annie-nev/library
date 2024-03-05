import json
from file_reader import FileReader


class JsonReader(FileReader):

    def read(self):
        with open(self.file_path) as json_file:
            file_content = json_file.read()
            content_as_dict = json.loads(file_content)
            print(content_as_dict.keys())

