from ..models.user_model import User

from flask import request

class UserController:
    
    @classmethod
    def get(cls, id_user):
        """Get a user by id"""
        user = User(id_user=id_user)
        result = User.get(user)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        """Get all users"""
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200

    @classmethod
    def create(cls):
        """Create a new user"""
        data = request.json
        
        user = User(**data)
        User.create(user)
        return {'message': 'User created successfully'}, 201

    @classmethod
    def update(cls, id_user):
        """Update a user"""
        data_parcial = request.json

        get = cls.get(id_user)

        data = get[0]
        
        for field, value in data_parcial.items():
            data[field] = value

        data['id_user'] = id_user
        

        user = User(**data)
        #print(user)
        User.update(user)
        
        return {'message': 'User updated successfully'}, 200
        
    @classmethod
    def delete(cls, id_user):
        """Delete a user"""
        user = User(id_user=id_user)
        
        User.delete(user)
        
        return {'message': 'User deleted successfully'}, 204