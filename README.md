## Introdução
Neste projeto estou apresentando como construir APIs REST com a linguagem Python utilizando o Microframework Flask e tambem o framework Endpoints.

## Instalação e configuração do ambiente
Para utilizar, primeiramente será necessário instalar:
- Python versao 3.6 ou superior
- MongoDB
- Postman (Para Testar as APIs)

Uma vez com o Python instalado, será necessário instalar algumas bibliotecas do Python, que são as seguintes:
- WebServices/Servidor HTML Flask         python -m pip install flask
- MongoDB                                 python -m pip install pymongo
- Endpoints API REST                      python -m pip install endpoints

## Executando o exemplos
Em ambos os exemplos devem ser executados a partir do MSDOS.
OBS: Antes de executá-los, não se esqueça de carregar o servidor do banco de dados MongoDB.

No caso do programa que utiliza o Flask, temos que executar o programa "exemplo_API.py" com a seguinte sintaxe:
- python exemplo_API.py
- Para testar, utilize a seguinte URL http://127.0.0.1:54321/

No caso do programa que utiliza o Endpoints, temos que executar com a seguinte sintaxe:
- endpoints --prefix=controllers --host=localhost:8000
- Para testar, utilize a seguinte URL http://127.0.0.1:54321/

Neste nossos exemplos, para ambos programas, você terá que utilizar o POSTMAN para realizar as requisições.

No POSTMAN:
- Leitura dos dados (GET):
    - Criar um requisição do tipo GET para a URL http://127.0.0.1:54321/itens
    - Executar e verificar a listagem dos dados, caso ja existam registros adicionados

- Criação de registros (POST):
    - Criar uma requisição do tipo POST para a URL http://127.0.0.1:54321/itens
    - No Headers: Content-Type application/json
    - No corpo (Body) da requisição, informar:
        { 
            "codigo": "A1",
            "descricao": "Parafusos 3/4",
            "valor": 53.00,
            "unidade": "cx",
            "quantidade": 10
        }
    - Ao chamar a requisição, será criado o registro desejado.

- Alteração de registros (PUT):
    - Criar uma requisição do tipo PUT para a URL http://127.0.0.1:54321/itens
    - No Headers: Content-Type application/json
    - No corpo (Body) da requisição, informar:
        { 
            "codigo": "A1",
            "descricao": "Parafusos 3/4 Sextavado",
            "valor": 45.00,
            "unidade": "cx",
            "quantidade": 9
        }
    - Ao chamar a requisição, será alterado o registro desejado.

- Eliminação de registros (DELETE):
    - Criar uma requisição do tipo DELETE para a URL http://127.0.0.1:54321/itens/A1
    - No Headers: Content-Type application/json
    - Na URL, após o /itens, deverá ser informado o código do produto a ser eliminado.
    - Ao chamar a requisição, será eliminado o registro desejado.
