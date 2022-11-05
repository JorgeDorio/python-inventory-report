from inventory_report.reports.simple_report import SimpleReport


def get_number_products(products: list) -> dict:
    companies = []
    counter = dict()
    for product in products:
        companies.append(product["nome_da_empresa"])

    for company in companies:
        counter[company] = companies.count(company)

    return counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list) -> str:
        number = get_number_products(products)
        report = SimpleReport.generate(products)
        report += "\nProdutos estocados por empresa:\n"
        for company in number:
            report += f"- {company}: {number[company]}\n"
        return report
