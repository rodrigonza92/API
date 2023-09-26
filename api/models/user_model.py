from ..database import DatabaseConnection

class User:
    """User model class"""
    
    def __init__(self, id_user = None, first_name = None, last_name = None, birthday = None, email = None, username = None, passwd = None):
        """Constructor method"""
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday    #El formato de fecha tiene que ser 1999-04-07
        self.email = email
        self.username = username
        self.password = passwd

    def serialize(self):
        return {
            "id_user": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "email": self.email,
            "username": self.username,
            "passwd": self.password,
        }

    @classmethod
    def get(cls, user):
        """Get a user by id
        Args:
            - user (user): user object with the id attribute
        Returns:
            - user: user object
        """

        query = """SELECT id_user, first_name, last_name, birthday, email, username, passwd FROM db_tif.usuario WHERE id_user = %s"""
        params = user.id_user,
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)

    
    @classmethod
    def get_all(cls):
        """Get all users
        Returns:
            - list: List of user objects
        """
        query = """SELECT id_user, first_name, last_name, birthday, email, username, passwd FROM db_tif.usuario"""

        results = DatabaseConnection.fetch_all(query)
        
        users = []
        if results is not None:
            for result in results:
                users.append(cls(*result))
        return users
    
    @classmethod
    def create(cls, user):
        """Create a new user
        Args:
            - user (user): user object
        """
        query = """INSERT INTO db_tif.usuario (first_name, last_name, birthday, email, username, passwd) VALUES (%s, %s, STR_TO_DATE(%s, "%Y-%m-%d"), %s, %s, %s)"""
        # La fecha debe ser del forma Año-mes-dia --> Ejemplo '2000-07-20'
        params = user.first_name, user.last_name, user.birthday, user.email, user.username, user.password,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        """Update a user
        Args:
            - user (user): user object
        """
        params = user.first_name, user.last_name, user.birthday, user.email, user.username, user.password, user.id_user,
        query = "UPDATE db_tif.usuario SET first_name = %s, last_name = %s, birthday = STR_TO_DATE(%s, '%d-%M-%Y'), email = %s, username = %s, passwd = %s WHERE id_user = %s;"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, user):
        """Delete a user
        Args:
            - user (user): user object with the id attribute
        """
        query = "DELETE FROM db_tif.usuario WHERE id_user = %s;"
        params = user.id_user,
        DatabaseConnection.execute_query(query, params=params)