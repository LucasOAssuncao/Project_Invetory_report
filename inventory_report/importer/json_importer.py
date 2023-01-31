import json


class CsvImporter:
    def import_data(path):
        with open(path) as file:
            return list(json.loads(file.read()))
