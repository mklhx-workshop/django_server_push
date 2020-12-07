# FROM node:latest
# WORKDIR /webapp/

# COPY webapp/package.json .
# COPY webapp/yarn.lock .
# RUN npm install

# COPY ./webapp/ ./webapp/

# RUN npm http-server

FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'webapp' folder the current working directory
WORKDIR /webapp/

# copy both 'package.json' and 'package-lock.json' (if available)
COPY webapp/package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]