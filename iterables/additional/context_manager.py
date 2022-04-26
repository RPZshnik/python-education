import os


class File:
    def __init__(self, file_name: str, file_mode="a+"):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.file_mode)
            return self
        except SyntaxError as e:
            self.create_file()
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def create_file(self):
        if os.path.isfile(self.file_name):
            pass
        else:
            createFile = self.file = open(self.file_name, "w+")
            if createFile:
                print(f'Created "{self.file_name}" file. File mode \'{self.file_mode}\'.')

    def remove_file(self):
        rm = os.remove(self.file_name)
        if rm == None:
            print(f"Removed \"{self.file_name}\" file.")

    def write(self, txt):
        if self.file.closed == False:
            self.file.write(txt)
            print(f"`{txt[:-2]}` added to {self.file_name}")

    def read(self):
        if self.file.closed == False and os.path.isfile(self.file_name):
            lines = self.file.readlines()
            items: list = []
            for line in lines:
                item = line.split(';')
                items.append({"name": item[0], "price": item[1], "quantity": item[2]})
            return items