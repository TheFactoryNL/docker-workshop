FROM node:latest
COPY * /tmp
WORKDIR /tmp
EXPOSE 3001
RUN npm i
ENTRYPOINT ["node", "index.js"]

#docker run -p 3001:3001 npmapi