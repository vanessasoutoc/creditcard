# Creditcard

Front-end e Backend responsável pela gestão de Cartões de Crédito. Teste técnico.

## Requisitos
[Docker](https://www.docker.com/get-started/)

## Docker

Utilize [Docker](https://www.docker.com/get-started/) para rodar as aplicações. Execute os comandos abaixo na pasta root.

`$ docker-compose build`

`$ docker-compose up`

## Frontend

Desenvolvido em [React](https://www.typescriptlang.org/pt/docs/handbook/react.html) e [Typescript](https://www.typescriptlang.org/)

Acesso em [http://localhost:8000](http://localhost:8000)


## Backend (api)

Desenvolvido em Python, utilizando o framework [FastApi](https://fastapi.tiangolo.com/)

Acesso em [http://localhost:8008/](http://localhost:8008/)

Documentação [http://localhost:8008/docs](http://localhost:8008/docs)

### Run Test

Start docker with commnad:

`$  docker-compose up -d --build`

And run test with command:

`$ docker-compose exec api pytest .`
