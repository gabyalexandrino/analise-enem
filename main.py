import os
import chardet
import dicionario
import pandas_gbq
import pandas as pd
from io import StringIO
from google.cloud import storage

# Configura o caminho para as credenciais do GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credentials.json"

# Instancia o cliente do Google Cloud Storage
storage_client = storage.Client()

# Nome do bucket e arquivo no GCP
BUCKET_NAME = "datadc"
FILE_NAME = "MICRODADOS_ENEM_2023.csv"
DATASET="enem"
PROJECT_ID="dc-finalproject"

def detect_encoding(bucket_name, blob_name):
    """Detecta a codificação de um arquivo no GCP."""
    try:
        # Obtém o objeto Blob no bucket
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        # Faz o download parcial do arquivo (até 10 MB)
        sample_size = 10 * 1024 * 1024  # 10 MB
        sample = blob.download_as_bytes(start=0, end=sample_size - 1)
        # Detecta a codificação do conteúdo
        result = chardet.detect(sample)
        return result['encoding']
    except Exception as e:
        print(f"Erro ao detectar a codificação: {e}")
        return None

def read_gcp_file(blob_name, file_encoding):
    """Lê o conteúdo de um arquivo no GCP e grava um novo conteúdo."""
    try:
        # Obtém o objeto Blob no bucket
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(blob_name)

        # Lê o conteúdo existente
        # Faz o download do conteúdo do arquivo como texto
        content = blob.download_as_text(encoding=file_encoding)

        # Converte o conteúdo para um DataFrame usando StringIO
        df = pd.read_csv(StringIO(content), sep=";", encoding=file_encoding)
        print("Dataframe gerado com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao acessar ou gravar o arquivo: {e}")
        return None
    
def load_to_bigquery(df, table_name, dataset, project_id):
    """
    Carrega um DataFrame para uma tabela no BigQuery.
    """
    try:
        table_id = f"{dataset}.{table_name}"
        pandas_gbq.to_gbq(df, table_id, project_id=project_id, if_exists="replace")
        print(f"DataFrame {table_name} carregado no BigQuery com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o DataFrame {table_name} no BigQuery: {e}")

if __name__ == "__main__":

    # Detecta a codificação do arquivo
    file_encoding = detect_encoding(BUCKET_NAME, FILE_NAME)
    if file_encoding:
        print(f"Codificação detectada: {file_encoding}")

    # Lê o arquivo do bucket e gera um DataFrame
    fato_microdados_enem_2023 = read_gcp_file(FILE_NAME, file_encoding)

    if fato_microdados_enem_2023 is not None:
        nome_tabela = "fato_microdados_enem_2023"
        # Carrega o DataFrame no BigQuery
        load_to_bigquery(fato_microdados_enem_2023, nome_tabela, DATASET, PROJECT_ID)
    
    # Itera sobre os DataFrames selecionados
    dataframes = [name for name, value in vars(dicionario).items() if not name.startswith("__")]
    
    # Itera sobre os DataFrames selecionados
    for name in dataframes[1:]:
        # Obtem o DataFrame diretamente do módulo "dicionario"
        dataframe = getattr(dicionario, name)

        # Carrega o DataFrame no BigQuery
        load_to_bigquery(dataframe, name, DATASET, PROJECT_ID)
            
