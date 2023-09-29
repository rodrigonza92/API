from ..database import DatabaseConnection

class Channel:

    def __init__(self, id_channel = None, nombre = None, id_server = None):
        self.id_channel = id_channel
        self.nombre = nombre
        self.id_server = id_server

    def serialize(self):
        return {
            "id_channel": self.id_channel,
            "nombre": self.nombre,
            "id_server": self.id_server
        }
    
    @classmethod
    def get(cls, channel):
        """Get a channel by id
        Args:
            - channel (channel): channel object with the id attribute
        Returns:
            - channel: channel object
        """

        query = """SELECT id_channel, nombre, id_server FROM db_tif.canal WHERE id_channel = %s"""
        params = channel.id_channel,
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)
    
    @classmethod
    def get_all(cls):
        """Get all channels
        Returns:
            - list: List of channel objects
        """
        query = """SELECT id_channel, nombre, id_server FROM db_tif.canal"""
        results = DatabaseConnection.fetch_all(query)

        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
        return channels
    
    @classmethod
    def create(cls, channel):
        """Create a new channel
        Args:
            - channel (channel): channel object
        """
        query = """INSERT INTO db_tif.canal (nombre, id_server) VALUES (%s, %s);"""

        params = channel.nombre, channel.id_server,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, channel):
        """Update a channel
        Args:
            - channel (channel): channel object
        """
        params = channel.nombre, channel.id_server,
        query = "UPDATE db_tif.canal SET nombre = %s, id_server = %s WHERE id_channel = %s;"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, channel):
        """Delete a channel
        Args:
            - channel (channel): channel object with the id attribute
        """

        query = "DELETE FROM db_tif.canal WHERE id_channel = %s;"
        params = channel.id_channel,
        DatabaseConnection.execute_query(query, params=params)