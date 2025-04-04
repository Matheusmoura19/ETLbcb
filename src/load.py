import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Função criada para salvar um DataFrame como um arquivo CSV.

    Parâmetros:
        df (pd.DataFrame): O DataFrame que deve ser salvo.
        nome_arquivo (str): Caminho e nome do arquivo de saída (ex: 'dados.csv').
        separador (str): Caractere usado como separador de colunas no CSV (ex: ',' ou ';').
        decimal (str): Caractere usado para representar o ponto decimal (ex: '.' ou ',').

    Saída esperada:
    O DataFrame deve ser salvo em um arquivo .csv
    
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return