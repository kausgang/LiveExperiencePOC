# FROM httpd:latest
FROM ubuntu/apache2:latest
COPY index.html /var/www/html/
COPY my-httpd.conf /usr/local/apache2/conf/httpd.conf

RUN a2enmod cgid

RUN /usr/sbin/apache2ctl stop
RUN /usr/sbin/apache2ctl start

EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]
