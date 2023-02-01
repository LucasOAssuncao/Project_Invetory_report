from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport
import pytest

AZUL = "\033[36m"
VERDE = "\033[32m"
VERMELHO = "\033[31m"
RE = "\033[0m"


@pytest.fixture
def product_list():
    product = [
        {
            "id": 1,
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corp",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
    ]
    return product


def test_decorar_relatorio(product_list):
    data = (
        f"{VERDE}Data de fabricação mais antiga:{RE} {AZUL}2021-02-18{RE}\n"
        f"{VERDE}Data de validade mais próxima:{RE} {AZUL}2023-09-17{RE}\n"
        f"{VERDE}Empresa com mais produtos:{RE} {VERMELHO}Target Corp{RE}"
    )

    assert data in ColoredReport(CompleteReport).generate(
        product_list
    )
    assert data in ColoredReport(SimpleReport).generate(
        product_list
    )
