import csv


class CsvImporter:
    def import_data(path):
        with open(path) as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))
