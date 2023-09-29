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

INSERT INTO db_tif.usuario (first_name, last_name, birthday, email, username, passwd)
VALUES
    ('Juan', 'Perez', '1990-05-15', 'juan@example.com', 'juanito', 'contrasena1'),
    ('Maria', 'Gonzalez', '1985-08-20', 'maria@example.com', 'maria123', 'contrasena2'),
    ('Carlos', 'Rodriguez', '1992-03-10', 'carlos@example.com', 'carlitos', 'contrasena3'),
    ('Laura', 'Lopez', '1988-12-05', 'laura@example.com', 'laurita', 'contrasena4'),
    ('Pedro', 'Martinez', '1995-07-25', 'pedro@example.com', 'pedrito', 'contrasena5'),
    ('Ana', 'Sanchez', '1993-02-18', 'ana@example.com', 'anita', 'contrasena6'),
    ('Luis', 'Torres', '1987-09-30', 'luis@example.com', 'lucho', 'contrasena7'),
    ('Sofia', 'Gomez', '1998-04-12', 'sofia@example.com', 'sofi', 'contrasena8'),
    ('Diego', 'Fernandez', '1994-06-08', 'diego@example.com', 'dieguito', 'contrasena9'),
    ('Elena', 'Hernandez', '1991-11-22', 'elena@example.com', 'elena123', 'contrasena10');

    INSERT INTO db_tif.servidor (nombre, descripcion)
VALUES
    ('Servidor de Cine', 'Ofrece películas y series en línea.'),
    ('Servidor de Juegos', 'Proporciona acceso a juegos en línea.'),
    ('Servidor de Música', 'Transmite música en línea.'),
    ('Servidor de Almacenamiento', 'Almacena archivos y documentos en la nube.'),
    ('Servidor de Chat', 'Facilita la comunicación en línea entre usuarios.');

    INSERT INTO db_tif.membresia_servidor (id_user, id_server)
VALUES
    (1,1),
    (1,2),
    (3,1),
    (3,4);

    INSERT INTO db_tif.mensaje (id_user, id_channel, fecha, mensaje)
VALUES (1, 1, NOW(), 'Hola a todos en el canal 1'),
		(3,1, NOW(), 'que parece grupo');
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