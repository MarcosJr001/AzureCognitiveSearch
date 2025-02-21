# Azure Cognitive Search: Utilizando AI Search para Indexação e Consulta de Dados

## Descrição do Projeto

Este projeto demonstra como usar o **Azure Cognitive Search** em conjunto com o **AI Search** para indexar e consultar dados. O objetivo é mostrar como o Azure Cognitive Search pode ser utilizado para criar um índice de pesquisa inteligente, aplicando técnicas de AI para enriquecer os resultados das consultas.

O projeto inclui:
- Criação de um índice no Azure Cognitive Search.
- Carregamento de dados de exemplo.
- Execução de consultas utilizando a API do Azure para realizar buscas avançadas, incluindo busca por similaridade e sugestões automáticas.

## Passo a Passo para Configuração de Pesquisa

### 1. Configuração do Ambiente Azure
1. Acesse o portal Azure e crie uma nova instância do **Azure Cognitive Search**.
2. Após a criação, obtenha as chaves de acesso e o endpoint da sua instância.
3. Instale o pacote `azure-search-documents` para interagir com a API usando o seguinte comando:

    ```bash
    pip install azure-search-documents
    ```

### 2. Preparação dos Dados
Utilize o arquivo `data/example_data.csv` para carregar dados no índice. Este arquivo contém informações de exemplo que serão indexadas, como produtos e suas descrições.

### 3. Criação de um Índice
Utilize o script `scripts/indexer_config.json` para definir o índice, incluindo os campos que serão pesquisáveis (por exemplo, nome, descrição) e como os dados serão organizados.

### 4. Carregamento de Dados
Carregue os dados no índice utilizando o script `scripts/upload_data.py`. Este script se conecta ao Azure Cognitive Search e faz o upload do arquivo CSV.

### 5. Consulta com AI Search
Para realizar consultas avançadas com AI Search, utilize o script `scripts/query_search.py`. Ele permite fazer buscas por palavras-chave, sugerir termos de pesquisa, e obter resultados relevantes utilizando técnicas de IA.

## Insights e Possibilidades de Ferramentas Beneficiadas

- **E-commerce**: Otimize a pesquisa de produtos, melhorando a experiência do cliente com sugestões inteligentes e busca por similaridade.
- **Sites de Conteúdo**: Melhore a pesquisa de artigos, vídeos e posts, com resultados mais relevantes e contextualizados.
- **Big Data**: Azure Cognitive Search pode ser utilizado para criar soluções de busca rápidas e eficientes em grandes volumes de dados não estruturados.

### Aprendizados Adquiridos
- Como configurar e utilizar o Azure Cognitive Search para indexação e consulta de dados.
- Como aplicar técnicas de AI Search para enriquecer a experiência de busca.
- Como lidar com grandes volumes de dados e otimizar a performance de pesquisa.
- Desafios enfrentados durante o processo de integração e soluções adotadas.

## Como Rodar o Projeto

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/Azure-Cognitive-Search-AI.git
    cd Azure-Cognitive-Search-AI
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure sua instância do Azure Cognitive Search e insira as credenciais no arquivo `scripts/config.py`.
4. Carregue os dados com:

    ```bash
    python scripts/upload_data.py
    ```

5. Execute uma consulta com:

    ```bash
    python scripts/query_search.py
    ```

## Contribuições

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções de bugs! Abra uma issue ou um pull request.
