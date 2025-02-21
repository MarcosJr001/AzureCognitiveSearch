from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Credenciais do Azure
endpoint = "https://<your-search-service-name>.search.windows.net"
index_name = "<your-index-name>"
api_key = "<your-api-key>"

# Inicializa o cliente de pesquisa
client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(api_key))

def search_query(query):
    # Realiza a consulta com AI Search
    results = client.search(query)
    for result in results:
        print(result)

if __name__ == "__main__":
    query = input("Digite sua pesquisa: ")
    search_query(query)
