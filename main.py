import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv

dados_bcb = requestApiBcb('20191')
salvarCsv(dados_bcb, 'src/datasets/meiosPagamentosTri.csv', ';', '.')