FROM node:latest
COPY . /tmp
WORKDIR /tmp
RUN npm i && npm run build
RUN npm install -g serve
EXPOSE 3000
ENTRYPOINT [ "serve", "-s", "build" ]
