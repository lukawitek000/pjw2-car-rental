#Build stage
FROM node:alpine

WORKDIR /app

COPY car-rental-app/package*.json /app/

RUN npm install -g @angular/cli

COPY . .

RUN npm run build

