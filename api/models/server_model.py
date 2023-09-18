from ..database import DatabaseConnection

class Server:

    def __init__(self, **kwargs):
        self.id_server = kwargs.get('id_server')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
        self.id_channel = kwargs.get('id_channel')


    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (server): server object with the id attribute
        Returns:
            - server: server object
        """

        query = """SELECT id_server, nombre, descripcion, id_channel 
        FROM server WHERE id_server = %s"""
        params = server.id_server,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        #else:
            #raise serverNotFound(server.server_id)
    
    @classmethod
    def get_all(cls):
        """Get all servers
        Returns:
            - list: List of server objects
        """
        query = """SELECT id_server, nombre, descripcion, id_channel 
        FROM server"""
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
        query = """INSERT INTO db_tif.servidor (nombre, descripcion, id_channel) VALUES (%s, %s, %s);"""
        
        # if server.special_features is not None:
        #     special_features = ','.join(server.special_features)
        # else:
        #     special_features = None
        
        # data = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]

        #if len(server.title) >= 3 and isinstance(server.language_id, int) and isinstance(server.rental_duration,int):

        params = server.nombre, server.descripcion, server.id_channel,
        DatabaseConnection.execute_query(query, params=params)
        #else:
            #raise InvalidDataError()

    @classmethod
    def update(cls, server):
        """Update a server
        Args:
            - server (server): server object
        """

        allowed_columns = {'id_server', 'nombre', 'descripcion', 'id_channel'}
        query_parts = []
        params = []
        for key, value in server.__dict__.items():
            if key in allowed_columns and value is not None:
                if key == 'special_features':
                    if len(value) == 0:
                        value = None
                    else:
                        value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(server.server_id)

        query = "UPDATE server SET " + ", ".join(query_parts) + " WHERE id_server = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, server):
        """Delete a server
        Args:
            - server (server): server object with the id attribute
        """

        query = "DELETE FROM server WHERE id_server = %s;"
        params = server.server_id,
        DatabaseConnection.execute_query(query, params=params)