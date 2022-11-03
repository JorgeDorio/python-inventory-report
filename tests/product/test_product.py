from inventory_report.inventory.product import Product

mockProduct = {
        "id": 1,
        "nome_do_produto":"Buds 3",
        "nome_da_empresa": "xiaomi",
        "data_de_fabricacao": "11/03/2022",
        "data_de_validade": "11/03/2023",
        "numero_de_serie": "1234560",
        "instrucoes_de_armazenamento": "Limpar semanalmente"
        }

def test_cria_produto():
    product = Product(mockProduct["id"], mockProduct["nome_do_produto"], mockProduct["nome_da_empresa"], mockProduct["data_de_fabricacao"], mockProduct["data_de_validade"], mockProduct["numero_de_serie"], mockProduct["instrucoes_de_armazenamento"])
    assert product.id == mockProduct["id"]
    assert product.nome_do_produto == mockProduct["nome_do_produto"]
    assert product.nome_da_empresa == mockProduct["nome_da_empresa"]
    assert product.data_de_fabricacao == mockProduct["data_de_fabricacao"]
    assert product.data_de_validade == mockProduct["data_de_validade"]
    assert product.numero_de_serie == mockProduct["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == mockProduct["instrucoes_de_armazenamento"]
