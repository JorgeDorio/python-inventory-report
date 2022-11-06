import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path: str) -> str:
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path) as report_file:
            return json.load(report_file)
