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


def get_number_products(products: list) -> dict:
    companies = set()
    for product in products:
        companies.add(product["nome_da_empresa"])
    print(companies)
    return {}


def get_more_products_company(products: list) -> str:
    companies = []
    for product in products:
        companies.append(product["nome_da_empresa"])
    return Counter(companies).most_common(1)[0][0]


class SimpleReport:
    @classmethod
    def generate(cls, products: list) -> str:
        older = get_older_fabrication(products)
        closer = get_closer_expiration(products)
        more_products = get_more_products_company(products)
        return (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {closer}\n"
            f"Empresa com mais produtos: {more_products}"
        )
