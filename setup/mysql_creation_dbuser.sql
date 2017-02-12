
# update settings.py accordingly
USERNAME="osmesh_user"
USERPASS="osmesh_1337"
DBNAME="osmesh_api"

# calling mysql
echo "CREATE database ${DBNAME};
CREATE USER '${USERNAME}'@'localhost' IDENTIFIED BY '${USERPASS}';
GRANT select,insert,update on ${DBNAME}.* TO '${USERNAME}'@'localhost';" > mysql_creation_tmp.sql

mysql -u root -p < mysql_creation_tmp.sql



###  CREATE DATABASE mydatabase CHARACTER SET utf8 COLLATE utf8_bin
