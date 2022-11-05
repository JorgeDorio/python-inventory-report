from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Buds 3 Pro",
        "Xiaomi",
        "03/11/2022",
        "03/11/2023",
        "a1b2c3",
        "Limpar uma vez por semana",
    )

    data = product.__repr__()

    assert data == (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} com validade "
        f"até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
