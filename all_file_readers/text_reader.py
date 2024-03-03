from file_reader import FileReader


class TextReader(FileReader):
    def read(self):
        file_content = open(self.file_path, "r")
        return file_content.read()

