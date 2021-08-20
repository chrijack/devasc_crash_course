FROM ubuntu:16.04
LABEL maintainer="Cisco Champion (user@domain.com)"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
EXPOSE 80 443
VOLUME /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
