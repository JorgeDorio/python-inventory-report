from inventory_report.inventory.product import Product
from .mocks import MockProduct


def test_cria_produto():
    mock = MockProduct()
    product = Product(
        mock.product["id"],
        mock.product["nome_do_produto"],
        mock.product["nome_da_empresa"],
        mock.product["data_de_fabricacao"],
        mock.product["data_de_validade"],
        mock.product["numero_de_serie"],
        mock.product["instrucoes_de_armazenamento"],
    )

    assert product.id == mock.product["id"]
    assert product.nome_do_produto == mock.product["nome_do_produto"]
    assert product.nome_da_empresa == mock.product["nome_da_empresa"]
    assert product.data_de_fabricacao == mock.product["data_de_fabricacao"]
    assert product.data_de_validade == mock.product["data_de_validade"]
    assert product.numero_de_serie == mock.product["numero_de_serie"]
    assert (
        product.instrucoes_de_armazenamento
        == mock.product["instrucoes_de_armazenamento"]
    )
