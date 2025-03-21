import requests
import pandas as pd

def busca_data(data):
    """
    Função para extrair os dados dos meios de pagamento 
    
    """
    url = f'https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json'

    req = requests.get(url)
    dados = req.json()

    df = pd.json_normalize(dados['value'])

    return print(df)



busca_data('20241')