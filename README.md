# Desafio programação - Desenvolvedor Python

# Ambiente de desenvolvimento
* Python 3.7
* MySQL Server 8.0.17 
  * O mesmo deverá estar instalado, no ar e com um usuário com permissões de DDL e DML.
* PyCharm 2021.1.2

# Instalação
* Clonar o repositório 
  * https://github.com/grmagalhaes/desafio-dev.git
* Criar um venv e habilitá-lo
* Instalar as dependências (django, mysql). Rodar dentro da pasta do repo.
    * pip -r requirements.txt
* Configurar as informações de conexão com a base de dados no arquivo settings.py dentro da pasta interna "project":  
    ```
    DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'desafio',
      'USER': 'desafio',
      'PASSWORD': 'desafio123',
      'HOST': 'localhost',
      'PORT': '3306',
      }
    }
    ```
    * para facilitar em script_db/create_db.sql há um script de criação de banco e usuário (este em localhost). Para criar o banco basta executar a linha abaixo:
    ```
    mysql -u root -p < CAMINHO_DO_PROJETO/script_db/create_db.sql
    ```
    * caso o mysql seja usado de outro host o script deverá ser alterado para o hostname do servidor de BD.
    * o script já dá permissão para a criação do banco de teste (test_desafio no caso)

    
* Executar os comandos dentro da pasta interna "project" para atualizar e migrar o esquema a partir do Django para o MySQL
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

# Execução do Projeto
* Para executar o projeto basta digitar o comando abaixo dentro da pasta interna "project"
    ```
    python manage.py runserver
    ```
* O projeto estará disponível em http://localhost:8000/
* O modo DEBUG ficará ligado em função do propósito do desafio

# Funcionamento do Projeto
* Para simplificar foi criada apenas uma tela onde:
  - A partir do botão "Escolher arquivo" o usuário poderá escolher o CNAB.txt (há verificação de formato)
  - Botão "Enviar" para fazer o envio do arquivo para o servidor. Após o parse e inserção na base a tabela é atualizada
  - Botão "Atualizar" para atualizar os valores da tabela
  - Botão "Limpar Base" para limpar a base de dados, facilitando os testes
  

# Teste do Projeto
* Para executar os testes basta digitar o comando abaixo dentro da pasta "project"
    ```
    python manage.py test
    ```
---

# Referência

Este desafio foi baseado neste outro desafio: https://github.com/ByCodersTec/desafio-dev
