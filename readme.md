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


## Backend (api)

Desenvolvido em Python, utilizando o framework [FastApi](https://fastapi.tiangolo.com/)


### Run Test

Start docker with commnad:

`$  docker-compose up -d --build`

And run test with command:

`$ docker-compose exec web pytest .`
