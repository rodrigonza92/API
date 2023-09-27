from ..database import DatabaseConnection

class Server:

    def __init__(self, id_server = None, nombre = None, descripcion = None):
        self.id_server = id_server
        self.nombre = nombre
        self.descripcion = descripcion

    
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
    def create(cls, server):
        """Create a new server
        Args:
            - server (server): server object
        """
        query = """INSERT INTO db_tif.servidor (nombre, descripcion, id_user, id_channel) VALUES (%s, %s, %s, %s);"""

        params = server.nombre, server.descripcion, server.id_user, server.id_channel,
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