# Creditcard

Front-end e Backend responsável pela gestão de Cartões de Crédito. Teste técnico.

## Requisitos
[Docker](https://www.docker.com/get-started/)

## Acesso Online

Deploy realizado via GitHub Actions.

[Frontend](http://31.220.62.96:8000/)

[Api](http://31.220.62.96:8008/docs)

## Utilizando Docker

Utilize [Docker](https://www.docker.com/get-started/) para rodar as aplicações. Execute os comandos abaixo na pasta root.

`$ docker-compose build`

`$ docker-compose up`

### Frontend

Desenvolvido em [React](https://www.typescriptlang.org/pt/docs/handbook/react.html) e [Typescript](https://www.typescriptlang.org/)

Acesso em [http://localhost:8000](http://localhost:8000)


### Backend (api)

Desenvolvido em Python, utilizando o framework [FastApi](https://fastapi.tiangolo.com/)

Acesso em [http://localhost:8008/](http://localhost:8008/)

Documentação [http://localhost:8008/docs](http://localhost:8008/docs)

### Run Test

Start docker with commnad:

`$  docker-compose up -d --build`

And run test with command:

`$ docker-compose exec api pytest --cov=src .`


## Rodando localmente

Obs: Não recomendado.
### Requisitos

- Python 3.11
- MongoDB 4.0.8
- NodeJS > 18

### Frontend

Acesse a pasta "frontend"

`$ npm install`

`$ npm start`

Acesso em [http://localhost:3003](http://localhost:3003)

### Api

Acesse a pasta "Api"

`$ pip install --no-cache-dir -r requirements.txt`

`$ python src/main.py`


#### Desenvolvido por

Vanessa Souto
