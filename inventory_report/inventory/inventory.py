from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory:
    def _open_file(self, path: str) -> list:
        if path.endswith(".csv"):
            with open(path) as data:
                reader = csv.DictReader(data)
                data = []
                for row in reader:
                    data.append(row)
            return data
        elif path.endswith(".json"):
            with open(path) as data:
                data = list(json.load(data))
            return data
        else:
            with open(path) as data:
                data = xmltodict.parse(data.read())["dataset"]["record"]
            return data

    @classmethod
    def import_data(cls, path: str, verbosity: str):
        data: list = cls._open_file(cls, path)
        if verbosity == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
