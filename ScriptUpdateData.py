from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Credenciais do Azure
endpoint = "https://<your-search-service-name>.search.windows.net"
index_name = "<your-index-name>"
api_key = "<your-api-key>"

# Inicializa o cliente de pesquisa
client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(api_key))

def upload_data(file_path):
    # Carregue o arquivo CSV e faça o upload dos dados para o índice
    # (Implementação do upload)

if __name__ == "__main__":
    upload_data("data/example_data.csv")
