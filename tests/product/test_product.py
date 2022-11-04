from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Buds 3 Pro",
        "Xiaomi",
        "03/11/2022",
        "03/11/2023",
        "a1b2c3",
        "Limpar uma vez por semana",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Buds 3 Pro"
    assert product.nome_da_empresa == "Xiaomi"
    assert product.data_de_fabricacao == "03/11/2022"
    assert product.data_de_validade == "03/11/2023"
    assert product.numero_de_serie == "a1b2c3"
    assert product.instrucoes_de_armazenamento == "Limpar uma vez por semana"
