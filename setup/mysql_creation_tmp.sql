CREATE database osmesh_api;
CREATE USER 'osmesh_user'@'localhost' IDENTIFIED BY 'osmesh_1337';
GRANT select,insert,update on osmesh_api.* TO 'osmesh_user'@'localhost';
