from ..database import DatabaseConnection

class Message:

    def __init__(self, id_message = None, id_user = None, id_channel = None, fecha = None, mensaje = None):
        self.id_message = id_message
        self.id_user = id_user
        self.id_channel = id_channel
        self.fecha = fecha
        self.mensaje = mensaje
    

    def serialize(self):
        return {
            "id_message": self.id_message,
            "id_user": self.id_user,
            "id_channel": self.id_channel,
            "fecha": self.fecha,
            "mensaje": self.mensaje
        }

    @classmethod
    def get(cls, message):
        """Get a message by id
        Args:
            - message (message): message object with the id attribute
        Returns:
            - message: message object
        """

        query = """SELECT id_user, id_channel, fecha, mensaje FROM db_tif.mensaje WHERE id_message = %s"""
        params = message.id_message,
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)
    
    @classmethod
    def get_all(cls):
        """Get all messages
        Returns:
            - list: List of message objects
        """
        query = """SELECT id_message, id_user, id_channel, fecha, mensaje FROM db_tif.mensaje"""
        results = DatabaseConnection.fetch_all(query)

        messages = []
        if results is not None:
            for result in results:
                messages.append(cls(*result))
        return messages
    
    @classmethod
    def create(cls, message):
        """Create a new message
        Args:
            - message (message): message object
        """
        query = """INSERT INTO db_tif.servidor (id_user, id_channel, fecha, mensaje) VALUES (%s, %s, %s, %s);"""

        params = message.id_user, message.id_channel, message.fecha, message.mensaje,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, message):
        """Update a message
        Args:
            - message (message): message object
        """

        params = message.id_user, message.id_channel, message.fecha, message.mensaje, message.id_message,
        query = "UPDATE db_tif.mensaje SET id_user = %s, id_channel = %s, fecha = %s, mensaje = %s WHERE id_message = %s;"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, message):
        """Delete a message
        Args:
            - message (message): message object with the id attribute
        """

        query = "DELETE FROM db_tif.message WHERE id_message = %s;"
        params = message.id_message,
        DatabaseConnection.execute_query(query, params=params)