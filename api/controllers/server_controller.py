from ..models.server_model import Server

from flask import request

class ServerController:
    
    @classmethod
    def get(cls, id_server):
        """Get a server by id"""
        server = Server(id_server=id_server)
        result = Server.get(server)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        """Get all servers"""
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200

    @classmethod
    def get_servers(cls, id_user):
        """Get all servers referidos a un ID de usuario"""
        server = Server(id_user=id_user)
        results = Server.get_servers(server)
        servers = []
        for server in results:
            servers.append(server.serialize())
        return servers, 200
    
    @classmethod
    def create(cls):
        """Create a new server"""
        data = request.json
        
        server = Server(**data)
        Server.create(server)
        return {'message': 'Server created successfully'}, 201

    @classmethod
    def update(cls, id_server):
        """Update a server"""
        data = request.json
        
        data['id_server'] = id_server

        server = Server(**data)
        
        Server.update(server)
        
        return {'message': 'Server updated successfully'}, 200

    @classmethod
    def delete(cls, id_server):
        """Delete a server"""
        server = Server(id_server=id_server)
        
        Server.delete(server)
        
        return {'message': 'Server deleted successfully'}, 204