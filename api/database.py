import mysql.connector

class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = cls._config['DATABASE_HOST'],
                user = cls._config['DATABASE_USERNAME'],
                port = cls._config['DATABASE_PORT'],
                password = cls._config['DATABASE_PASSWORD']
            )

        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config
    
    @classmethod
    def create_bd(cls):
        cursor = cls.get_connection().cursor()
        query = """CREATE DATABASE IF NOT EXISTS db_tif;

CREATE TABLE IF NOT EXISTS db_tif.usuario (
    id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL, 
    last_name VARCHAR (255) NOT NULL,
    birthday DATE NOT NULL,
    email VARCHAR (255) NOT NULL,
    username VARCHAR (255) NOT NULL,
    passwd VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS db_tif.servidor (
    id_server INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (255) NOT NULL,
    descripcion VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS db_tif.canal (
    id_channel INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    id_server INT NOT NULL,
    FOREIGN KEY (id_server) REFERENCES db_tif.servidor (id_server) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS db_tif.mensaje (
    id_message INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    id_channel INT NOT NULL,
    fecha DATETIME NOT NULL,
    mensaje VARCHAR (255) NOT NULL,
    FOREIGN KEY (id_user) REFERENCES db_tif.usuario (id_user) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_channel) REFERENCES db_tif.canal (id_channel) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS db_tif.membresia_servidor (
    id_user INT NOT NULL,
    id_server INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES db_tif.usuario (id_user) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_server) REFERENCES db_tif.servidor (id_server) ON DELETE CASCADE ON UPDATE CASCADE
);
        """
        cursor.execute(query)
        cls.close_connection()

    @classmethod
    def execute_query(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        
        return cursor.fetchone()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None