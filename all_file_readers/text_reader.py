"""
    Purpose: Implements TextReader class
    Author: Annie_nev
    Created:3.3.2024
"""
from file_reader import FileReader


class TextReader(FileReader):
    """
     Implements TextReader functions
    """
    def read(self):
        """
        reads text files
        :return: text file content
        """
        file_content = open(self.file_path, "r")
        return file_content.read()

    # TODO: change the return into print in bugfix
