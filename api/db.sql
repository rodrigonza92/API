--                        DATOS PARA REALIZAR TEST DE LA APP

-- DATOS PARA USUARIOS
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

-- PARA SERVIDORES

INSERT INTO db_tif.servidor (nombre, descripcion)
VALUES
    ('Servidor de Cine', 'Ofrece películas y series en línea.'),
    ('Servidor de Juegos', 'Proporciona acceso a juegos en línea.'),
    ('Servidor de Música', 'Transmite música en línea.'),
    ('Servidor de Almacenamiento', 'Almacena archivos y documentos en la nube.'),
    ('Servidor de Chat', 'Facilita la comunicación en línea entre usuarios.');

-- PARA MEMBRESIA_SERVIDOR    
    
INSERT INTO db_tif.membresia_servidor (id_user, id_server)
VALUES
    (1,1),
    (1,2),
    (3,1),
    (3,4);   

-- PARA CANALES

INSERT INTO db_tif.canal (nombre, id_server)
VALUES ('Canal 1', 1),
       ('Canal 2', 2),
       ('Canal 3', 1);