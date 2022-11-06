import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path: str) -> str:
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as report_file:
            return xmltodict.parse(report_file.read())["dataset"]["record"]
