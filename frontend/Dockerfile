FROM node:18-alpine

ADD package.json /package.json

RUN apk add g++ make py3-pip
ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
RUN npm install

WORKDIR /app
ADD . /app

EXPOSE 8003
EXPOSE 35729

ENTRYPOINT ["/bin/sh", "/app/run.sh"]
CMD ["start"]
