"""
    Purpose: Implements JsonReader class
    Author: Annie_nev
    Created:5.3.2024
"""
import json
from file_reader import FileReader


class JsonReader(FileReader):
    """
     Inherits from FileReader abstract class
     and replaces read function
    """

    def read(self):
        """
        prints json file keys
        """
        with open(self.file_path) as json_file:
            file_content = json_file.read()
            content_as_dict = json.loads(file_content)
            print(content_as_dict.keys())

