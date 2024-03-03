"""
Purpose: Implements FileReader class
Author: Annie_nev
Created:3.3.2024
"""

from abc import abstractmethod, ABC
import os


class FileReader(ABC):
    """
      Abstraction for various file readers
    """
    def __init__(self, file_path: str):
        """
        :param file_path: Gets file path as str
        """
        if os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise Exception("File path does not ")

    def size(self) -> int:
        """
        Finds file size according to file path
        :return: File size in bytes
        """
        return os.path.getsize(self.file_path)

    def name(self) -> str:
        """
        finds file name from path
        :return: File name and type
        """
        return os.path.basename(self.file_path)

    @abstractmethod
    def read(self):
        """
        Responsible for reading files and returning their contents.
        """
        pass
