from ..database import DatabaseConnection

class Message:

    def __init__(self, **kwargs):
        self.id_message = kwargs.get('id_message')
        self.id_channel = kwargs.get('id_channel')
        self.id_user = kwargs.get('id_user')
        self.mensaje = kwargs.get('mensaje')
    

    @classmethod
    def get(cls, msg):
        """Get a msg by id
        Args:
            - msg (msg): msg object with the id attribute
        Returns:
            - msg: msg object
        """

        query = """SELECT id_message, id_channel, id_user, mensaje 
        FROM mensaje WHERE id_message = %s"""
        params = msg.msg_id,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        #else:
            #raise msgNotFound(msg.msg_id)
    
    @classmethod
    def get_all(cls):
        """Get all msgs
        Returns:
            - list: List of msg objects
        """
        query = """SELECT id_message, id_channel, id_user, mensaje
        FROM mensaje"""
        results = DatabaseConnection.fetch_all(query)

        msgs = []
        if results is not None:
            for result in results:
                msgs.append(cls(*result))
        return msgs
    
    @classmethod
    def create(cls, msg):
        """Create a new msg
        Args:
            - msg (msg): msg object
        """
        query = """INSERT INTO mensaje (id_message, id_channel, id_user, mensaje) 
        VALUES (%s, %s, %s, %s)"""
        
        # if msg.special_features is not None:
        #     special_features = ','.join(msg.special_features)
        # else:
        #     special_features = None
        
        # data = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]

        # if len(msg.title) >= 3 and isinstance(msg.language_id, int) and isinstance(msg.rental_duration,int):

        params = msg.id_messaje, msg.id_channel, msg.id_user, msg.mensaje
        DatabaseConnection.execute_query(query, params=params)
        # else:
        #     raise InvalidDataError()

    @classmethod
    def update(cls, msg):
        """Update a msg
        Args:
            - msg (msg): msg object
        """

        allowed_columns = {'id_message', 'id_channel', 'id_user', 'mensaje'}
        query_parts = []
        params = []
        for key, value in msg.__dict__.items():
            if key in allowed_columns and value is not None:
                if key == 'special_features':
                    if len(value) == 0:
                        value = None
                    else:
                        value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(msg.msg_id)

        query = "UPDATE mensaje SET " + ", ".join(query_parts) + " WHERE id_message = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, msg):
        """Delete a msg
        Args:
            - msg (msg): msg object with the id attribute
        """

        query = "DELETE FROM mensaje WHERE id_message = %s;"
        params = msg.id_message,
        DatabaseConnection.execute_query(query, params=params)