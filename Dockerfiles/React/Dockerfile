FROM node:16.15.1


WORKDIR /usr/src/app

COPY --chown=node:node package.json .
RUN npm cache verify
RUN npm install || true

COPY --chown=node:node . .
USER node


RUN chmod 777  /usr/src/app/node_modules/.cache/.eslintcache


CMD ["npm", "start"]
