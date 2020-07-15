FROM node:lts-alpine as build-stage
WORKDIR /app/
COPY frontend/package.json /app/
RUN npm install
COPY frontend /app/
RUN npm run build

# !# этап production (production-stage)
FROM nginx:stable-alpine as production-stage
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

#* FROM nginx:stable-alpine as production-stage
#* COPY --from=build-stage /app/dist /usr/share/nginx/html
#* EXPOSE 80
#* CMD ["nginx", "-g", "daemon off;"]