# Desafio Tecnico da Tunts.Rocks 2024

- Link público da planilha
    ```
    https://docs.google.com/spreadsheets/d/1M7IPCF1Nm045sXvFT_TPZwDQykaXKgoxpsRoGWVYoI4/edit#gid=0
    ```
    
### Instalar

- Clonar o repositório
    ```bash
    git clone https://github.com/carlosfernandescrypt/desafio-tecnico-tuntsrocks-2024.git
    ```
- Navegue até o repositório clonado
- Instale as bibliotecas necessarias usando pip:
    ```pip
    pip install -r requirements.txt
    ```
- Execute:
    ```python
    python main.py
    ```

## Como integrar a API do Google Sheets

- Lembrando que você deverá ter as suas credenciais de autenticação do Google Sheets APIs, assim como também ativar a API do Google Drive
- #### Para saber como ativar suas APIs, siga os seguintes passos:

- #### 1. Crie um novo projeto no Google Cloud Console
      Acesse o Google Cloud Console.
      Clique em “Select a project” no canto superior direito.
      Clique em “NEW PROJECT” no canto superior direito da janela pop-up.
      Dê um nome ao seu projeto e clique em “CREATE”.

- #### 2. Habilite a API do Google Sheets
        No painel de navegação à esquerda, clique em “Library”.
        Pesquise por “Google Sheets API” e clique no resultado correspondente.
        Clique em “ENABLE”.

- #### 3. Crie credenciais
        No painel de navegação à esquerda, clique em “Credentials”.
        Clique em “CREATE CREDENTIALS” e selecione “Service account”.
        Preencha os detalhes necessários (nome da conta de serviço, descrição, etc.) e clique em “CREATE”.
        Na próxima tela, você pode selecionar a função desejada. Para fins de leitura e gravação em uma planilha, você pode selecionar “Editor”. Clique em “CONTINUE”.
        Clique em “DONE” na próxima tela.

- #### 4. Baixe o arquivo JSON
        Você será redirecionado para a página de detalhes da conta de serviço. Clique no e-mail da conta de serviço que você acabou de criar.
        Clique na guia “KEYS”.
        Clique em “ADD KEY” e selecione “JSON”. O arquivo JSON será baixado automaticamente.

- #### 5. Compartilhe a planilha do Google Sheets com a conta de serviço
        Abra a planilha do Google Sheets que você deseja ler/escrever.
        Clique em “Share” no canto superior direito.
        Insira o e-mail da conta de serviço (você pode encontrar isso no arquivo JSON baixado anteriormente) e clique em “Done”.


