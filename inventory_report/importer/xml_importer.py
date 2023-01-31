import xmltodict


class CsvImporter:
    def import_data(path):
        with open(path) as file:
            return list(xmltodict.parse(file.read())['dataset']['record'])
