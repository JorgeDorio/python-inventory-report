from inventory_report.inventory.product import Product
from ..product.mocks import MockProduct


def test_relatorio_produto():
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

    data = product.__repr__()

    assert data == (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} com validade "
        f"até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
