from ..database import DatabaseConnection

class Server:

    def __init__(self, id_server = None, nombre = None, descripcion = None, id_user = None):
        self.id_server = id_server
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_user = id_user

    
    def serialize(self):
        return {
            "id_server": self.id_server,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
        }

    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (server): server object with the id attribute
        Returns:
            - server: server object
        """

        query = """SELECT id_server, nombre, descripcion, id_user, id_channel FROM db_tif.servidor WHERE id_server = %s"""
        params = server.id_server,
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)
    
    @classmethod
    def get_all(cls):
        """Get all servers
        Returns:
            - list: List of server objects
        """
        query = """SELECT id_server, nombre, descripcion FROM db_tif.servidor"""
        results = DatabaseConnection.fetch_all(query)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers

    @classmethod
    def get_servers(cls, server):
        """Get a server by id
        Args:
            - server (server): server object with the id attribute
        Returns:
            - server: server object
        """

        query = f"SELECT db_tif.servidor.id_server, db_tif.servidor.nombre FROM db_tif.servidor INNER JOIN db_tif.membresia_servidor ON db_tif.servidor.id_server = db_tif.membresia_servidor.id_server WHERE db_tif.membresia_servidor.id_user = {server.id_user};"
    
        results = DatabaseConnection.fetch_all(query)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers
    
    @classmethod
    def create(cls, server, user_id):
        """Create a new server and return its ID along with the user ID
        Args:
            - server (server): server object
            - user_id (int): ID of the user who created the server
        Returns:
            - int: ID of the newly created server
        """

        #Si existe el id del usuario que crea el servidor
        if user_id:
            #Creo un nuevo servidor con el id del usuario logueado
            query = """INSERT INTO db_tif.servidor (nombre, descripcion) VALUES (%s, %s);"""
            params = server.nombre, server.descripcion,
            DatabaseConnection.execute_query(query, params=params)

            #Capturo el id del ultimo servidor creado
            query2 = """SELECT MAX(id_server) AS id FROM db_tif.servidor;"""
            id_server = DatabaseConnection.execute_query(query2)

            #Creo un registro de membresia con el id del usuario logueado y el ultimo id de server creado
            query3 = """INSERT INTO db_tif.membresia_servidor (id_user, id_server) VALUES (%s, %s)"""
            params3 = user_id, id_server,
            DatabaseConnection.execute_query(query3, params=params3)
            
        else:
            #En el caso que el usuario no este logueado, se crea el servidor sin id
            query = """INSERT INTO db_tif.servidor (nombre, descripcion) VALUES (%s, %s);"""

            params = server.nombre, server.descripcion,
            DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def update(cls, server):
        """Update a server
        Args:
            - server (server): server object
        """

        params = server.nombre, server.descripcion, server.id_user, server.id_channel, server.id_server,
        query = "UPDATE db_tif.servidor SET nombre = %s, descripcion = %s, id_user = %s, id_channel = %s WHERE id_server = %s;"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, server):
        """Delete a server
        Args:
            - server (server): server object with the id attribute
        """

        query = "DELETE FROM db_tif.servidor WHERE id_server = %s;"
        params = server.id_server,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def server_user(cls, server):
        """Get a server by id
        Args:
            - server (server): server object with the id attribute
        Returns:
            - server: server object
        """

        query = """SELECT id_server, nombre, descripcion FROM db_tif.servidor WHERE id_server = %s"""
        params = server.id_server, server.id_user
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)