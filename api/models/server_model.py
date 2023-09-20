from ..database import DatabaseConnection

class Server:

<<<<<<< HEAD
    def __init__(self, id_server = None, nombre = None, descripcion = None, id_channel = None):
        """Constructor method"""
        self.id_server = id_server
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_channel = id_channel

=======
    def __init__(self, id_server = None, nombre = None, descripcion = None, id_channel = None, id_user = None):
        self.id_server = id_server
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_user = id_user
        self.id_channel = id_channel
    
>>>>>>> Rodrigo
    def serialize(self):
        return {
            "id_server": self.id_server,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
<<<<<<< HEAD
=======
            "id_user": self.id_user,
>>>>>>> Rodrigo
            "id_channel": self.id_channel
        }

    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (server): server object with the id attribute
        Returns:
            - server: server object
        """

<<<<<<< HEAD
        query = """SELECT nombre, descripcion, id_channel FROM db_tif.servidor WHERE id_server = %s"""
        params = server.id_server,
        result = DatabaseConnection.fetch_one(query, params=params)
        
=======
        query = """SELECT id_server, nombre, descripcion, id_user, id_channel FROM db_tif.servidor WHERE id_server = %s"""
        params = server.id_server,
        result = DatabaseConnection.fetch_one(query, params=params)

>>>>>>> Rodrigo
        return cls(*result)
    
    @classmethod
    def get_all(cls):
        """Get all servers
        Returns:
            - list: List of server objects
        """
<<<<<<< HEAD
        query = """SELECT id_server, nombre, descripcion, id_channel FROM db_tif.servidor"""
        
=======
        query = """SELECT id_server, nombre, descripcion, id_user, id_channel FROM db_tif.servidor"""
>>>>>>> Rodrigo
        results = DatabaseConnection.fetch_all(query)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers
    
    @classmethod
    def create(cls, server):
        """Create a new server
        Args:
            - server (server): server object
        """
<<<<<<< HEAD
        query = """INSERT INTO db_tif.servidor (nombre, descripcion, id_channel) VALUES (%s, %s, %s);"""
        
        params = server.nombre, server.descripcion, server.id_channel,
        DatabaseConnection.execute_query(query, params=params)
        
=======
        query = """INSERT INTO db_tif.servidor (nombre, descripcion, id_user, id_channel) VALUES (%s, %s, %s, %s);"""

        params = server.nombre, server.descripcion, server.id_user, server.id_channel,
        DatabaseConnection.execute_query(query, params=params)

>>>>>>> Rodrigo
    @classmethod
    def update(cls, server):
        """Update a server
        Args:
            - server (server): server object
        """

<<<<<<< HEAD
        params = server.nombre, server.descripcion, server.id_channel, server.id_server,
        query = "UPDATE db_tif.servidor SET nombre = %s, descripcion = %s, id_channel = %s WHERE id_server = %s;"
=======
        params = server.nombre, server.descripcion, server.id_user, server.id_channel, server.id_server,
        query = "UPDATE db_tif.servidor SET nombre = %s, descripcion = %s, id_user = %s, id_channel = %s WHERE id_server = %s;"
>>>>>>> Rodrigo
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, server):
        """Delete a server
        Args:
            - server (server): server object with the id attribute
        """

<<<<<<< HEAD
        query = "DELETE FROM db_tif.servidor WHERE id_server = %s;"
=======
        query = "DELETE FROM db_tif.server WHERE id_server = %s;"
>>>>>>> Rodrigo
        params = server.id_server,
        DatabaseConnection.execute_query(query, params=params)