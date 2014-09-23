# mysql
#
# VERSION               0.1

FROM ubuntu:14.04
MAINTAINER Werner R. Mendizabal "werner.mendizabal@rackspace.com"

RUN apt-get update

RUN apt-get install -y mysql-server

RUN sed -i "s/^bind-address.*/bind-address = 0.0.0.0/g" /etc/mysql/my.cnf

RUN service mysql start && mysql -u root -e "CREATE DATABASE keystone;"

RUN service mysql start && mysql -u root -e "GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'0.0.0.0' IDENTIFIED BY 'password';"

RUN service mysql start && mysql -u root -e "GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'password';"

RUN service mysql start && mysql -u root -e "SET GLOBAL sql_mode = 'TRADITIONAL';"

EXPOSE 3306

CMD service mysql start && tail -F mysql.log -F mysql.err
