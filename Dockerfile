FROM alpine:3.14

RUN apk update && apk add --no-cache \
    apache2 openrc \
    php8-apache2 \
    php8 \
    php8-cli \
    php8-common \
    php8-ctype \
    php8-curl \
    php8-dom \
    php8-gd \
    php8-iconv \
    php8-intl \
    php8-json \
    php8-mbstring \
    php8-opcache \
    php8-pdo \
    php8-xml \
    php8-zip \
    php8-mysqli \
    php8-session \
    php8-tokenizer \
    php8-fileinfo \
    php8-openssl \
    php8-xmlreader \
    php8-xmlwriter \
    php8-xsl \
    php8-soap \
    php8-sodium \
    php8-exif \
    php8-phar \
    php8-pdo_mysql \
    php8-mysqli \
    php8-simplexml \
    mariadb-client \
    ghostscript 

EXPOSE 8000
EXPOSE 80

#Renomeando php
RUN mv /usr/bin/php8 /usr/bin/php

#Instalação do composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"

RUN php -r "if (hash_file('sha384', 'composer-setup.php') === 'e21205b207c3ff031906575712edab6f13eb0b361f2085f1f1237b7126d785e826a450292b6cfd1d64d92e6563bbde02') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

RUN php composer-setup.php

RUN php -r "unlink('composer-setup.php');"

RUN mv composer.phar /usr/local/bin/composer

#Instalando o vim
RUN apk add vim

#Copiando o projeto para a pasta project
COPY . /var/www/localhost/htdocs/project

RUN chmod 777 -R /var/www/localhost/htdocs/project

#Adicionando minha configuração personalizada do apache2
RUN cp /var/www/localhost/htdocs/project/example.conf /etc/apache2/conf.d/example.conf

#Configurando o apache2, habilitando o rewrite
RUN sed -i 's/#LoadModule rewrite_module modules\/mod_rewrite.so/LoadModule rewrite_module modules\/mod_rewrite.so/' /etc/apache2/httpd.conf

WORKDIR /var/www/localhost/htdocs/project

RUN composer install

CMD mkdir /run/openrc/ && touch /run/openrc/softlevel && openrc\
    && /etc/init.d/apache2 start \
    && tail -f /var/log/apache2/error.log
