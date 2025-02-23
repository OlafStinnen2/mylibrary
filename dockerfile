FROM node:latest
WORKDIR /app
COPY express-app/* .
RUN npm install
#COPY . /express-app
EXPOSE 8080
CMD ["node", "app.js"]

