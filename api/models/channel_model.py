from ..database import DatabaseConnection

class Channel:

    def __init__(self, **kwargs):
        self.id_channel = kwargs.get('id_channel')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')

    @classmethod
    def get(cls, channel):
        """Get a channel by id
        Args:
            - channel (channel): channel object with the id attribute
        Returns:
            - channel: channel object
        """

        query = """SELECT id_channel, nombre, descripcion
        FROM canal WHERE id_channel = %s"""
        params = channel.id_channel,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        #else:
            #raise channelNotFound(channel.channel_id)
    
    @classmethod
    def get_all(cls):
        """Get all channels
        Returns:
            - list: List of channel objects
        """
        query = """SELECT id_channel, nombre, descripcion
        FROM canal"""
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
        query = """INSERT INTO db_tif.canal (nombre, descripcion) VALUES (%s, %s);"""
        
        # if channel.special_features is not None:
        #     special_features = ','.join(channel.special_features)
        # else:
        #     special_features = None
        
        # data = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]

        #if len(channel.title) >= 3 and isinstance(channel.language_id, int) and isinstance(channel.rental_duration,int):

        params = channel.id_channel, channel.nombre, channel.descripcion
        DatabaseConnection.execute_query(query, params=params)
        #else:
            #raise InvalidDataError()

    @classmethod
    def update(cls, channel):
        """Update a channel
        Args:
            - channel (channel): channel object
        """

        allowed_columns = {'id_channel', 'nombre', 'descripcion'}
        query_parts = []
        params = []
        for key, value in channel.__dict__.items():
            if key in allowed_columns and value is not None:
                if key == 'special_features':
                    if len(value) == 0:
                        value = None
                    else:
                        value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(channel.id_channel)

        query = "UPDATE canal SET " + ", ".join(query_parts) + " WHERE id_channel = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, channel):
        """Delete a channel
        Args:
            - channel (channel): channel object with the id attribute
        """

        query = "DELETE FROM canal WHERE id_channel = %s;"
        params = channel.id_channel,
        DatabaseConnection.execute_query(query, params=params)