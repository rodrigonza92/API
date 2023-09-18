from ..database import DatabaseConnection

class User:
    """User model class"""
    
    # def __init__(self, **kwargs):
    #     self.id_user = kwargs.get('id_user')
    #     self.first_name = kwargs.get('first_name')
    #     self.last_name = kwargs.get('last_name')
    #     self.birthday = kwargs.get('birthday')
    #     self.email = kwargs.get('email')
    #     self.username = kwargs.get('username')
    #     self.password = kwargs.get('passwd')
    #     self.id_server = kwargs.get('id_server')
    
    def __init__(self, id_user = None, first_name = None, last_name = None, 
                 birthday = None, email = None, username = None, passwd = None, id_server = None):
        """Constructor method"""
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.username = username
        self.password = passwd
        self.id_server = id_server

    def serialize(self):
        return {
            "id_user": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "email": self.email,
            "username": self.username,
            "passwd": self.password,
            "id_server": self.id_server
        }

    @classmethod
    def get(cls, user):
        """Get a user by id
        Args:
            - user (user): user object with the id attribute
        Returns:
            - user: user object
        """

        query = """SELECT id_user, first_name, last_name, birthday, email, username, passwd, id_server FROM db_tif.usuario WHERE id_user = %s"""
        params = user.id_user,
        result = DatabaseConnection.fetch_one(query, params=params)

        return cls(*result)
        #else:
            #raise UserNotFound(user.user_id)
    
    @classmethod
    def get_all(cls):
        """Get all users
        Returns:
            - list: List of user objects
        """
        query = """SELECT id_user, first_name, last_name, birthday, email, username, passwd, id_server FROM db_tif.usuario"""

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
        query = """INSERT INTO db_tif.usuario (first_name, last_name, birthday, email, username, passwd, id_server) VALUES (%s, %s, STR_TO_DATE(%s, '%d-%M-%Y'), %s, %s, %s, %s)"""

        params = user.first_name, user.last_name, user.birthday, user.email, user.username, user.password, user.id_server,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        """Update a user
        Args:
            - user (user): user object
        """

        allowed_columns = {'first_name', 'last_name', 'birthday', 'email', 'username', 'passwd', 'id_server'}
        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(user.id_user)

        query = "UPDATE db_tif.usuario SET " + ", ".join(query_parts) + " WHERE id_user = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, user):
        """Delete a user
        Args:
            - user (user): user object with the id attribute
        """

        query = "DELETE FROM usuario WHERE id_user = %s;"
        params = user.user_id,
        DatabaseConnection.execute_query(query, params=params)