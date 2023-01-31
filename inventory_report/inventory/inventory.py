from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, string_type):
        if "csv" in path:
            data = CsvImporter.import_data(path)

        if "json" in path:
            data = JsonImporter.import_data(path)

        if "xml" in path:
            data = XmlImporter.import_data(path)

        if string_type == "completo":
            return CompleteReport.generate(data)
        else:
            return SimpleReport.generate(data)
