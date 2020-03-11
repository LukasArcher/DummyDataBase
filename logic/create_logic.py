from files_handler.files_handler import FilesHandler


class CreateLogic:
    def __init__(self):
        self.fh = FilesHandler()

    def create(self, document_name, columns):
        self.fh.create_file_and_write(f"{document_name}.ddo", ','.join(columns))

    def add_values(self, values, document_name):
        self.fh.add_to_file(f"{document_name}.ddo", ','.join(values))

    def select_column(self, column, document_name):
        self.fh.select_from_file(f"{document_name}.ddo", ','.join(column))

    def delete(self, document_name, column, value):
        self.fh.delete_from_file(f"{document_name}.ddo", column, value)

    def export(self, document_names):
        self.fh.export_files(document_names)

    def import_from_path(self, file_path):
        self.fh.import_files(file_path)

    def json_creator(self, document_name):
        self.fh.json_converter(document_name)
