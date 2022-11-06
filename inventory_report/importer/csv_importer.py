import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path: str) -> str:
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path) as report_file:
            return list(csv.DictReader(report_file))
