FROM node:latest

WORKDIR /app
ADD webserver/package.json /app/package.json
RUN npm config set registry https://registry.npmjs.org
RUN npm install

EXPOSE 3000

CMD ["npm", "run", "start"]