-- create schemas
CREATE SCHEMA db_tif;

-- create tables
CREATE TABLE db_tif.usuario (
	id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL, 
	last_name VARCHAR (255) NOT NULL,
	birthday DATE NOT NULL,
	email VARCHAR (255) NOT NULL,
	username VARCHAR (255) NOT NULL,
	passwd VARCHAR (255) NOT NULL
);

CREATE TABLE db_tif.mensaje (
	id_message INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	id_user INT NOT NULL,
	fecha DATETIME NOT NULL,
	mensaje VARCHAR (255) NOT NULL,
	FOREIGN KEY (id_user) REFERENCES db_tif.usuario (id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE db_tif.canal (
	id_channel INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR (255) NOT NULL,
	descripcion VARCHAR (255) NOT NULL,
    id_message INT NOT NULL,
    FOREIGN KEY (id_message) REFERENCES db_tif.mensaje (id_message) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE db_tif.servidor (
	id_server INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR (255) NOT NULL,
	descripcion VARCHAR (255) NOT NULL,
    id_user INT NOT NULL,
	id_channel INT NOT NULL,
	FOREIGN KEY (id_user) REFERENCES db_tif.usuario (id_user) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_channel) REFERENCES db_tif.canal (id_channel) ON DELETE CASCADE ON UPDATE CASCADE
);