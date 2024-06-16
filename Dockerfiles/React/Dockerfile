FROM node:16.15.1

WORKDIR /usr/src/app

COPY --chown=node:node ./front-react/package.json .

RUN npm i

COPY ./front-react ./

ENTRYPOINT ["npm"]
