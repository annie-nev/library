"""
Purpose: Implements TextReader class
Author: Annie_nev
Created:3.3.2024
"""
from file_reader import FileReader


class TextReader(FileReader):
    """
     Inherits from FileReader class
     replaces read function to be compatible with txt file
    """
    def read(self):
        """
        prints text file content
        """
        file_content = open(self.file_path, "r")
        print(file_content.read())

