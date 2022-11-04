from typing import Counter


def get_older_fabrication(products: list) -> str:
    dates = []
    for product in products:
        dates.append(product["data_de_fabricacao"])
    return min(dates)


def get_closer_expiration(products: list) -> str:
    dates = []
    for product in products:
        dates.append(product["data_de_validade"])
    return min(dates)


def get_more_products_company(products: list) -> str:
    companies = []
    for product in products:
        companies.append(product["nome_da_empresa"])
    return Counter(companies).most_common(1)[0][0]


class SimpleReport:
    @classmethod
    def generate(cls, products: list) -> str:
        return (
            f"Data de fabricação mais antiga: {get_older_fabrication(products)}\n"
            f"Data de validade mais próxima: {get_closer_expiration(products)}\n"
            f"Empresa com mais produtos: {get_more_products_company(products)}"
        )
