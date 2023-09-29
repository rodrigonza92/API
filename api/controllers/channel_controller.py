from ..models.channel_model import Channel

from flask import request

class ChannelController:
    
    @classmethod
    def get(cls, id_channel):
        """Get a channel by id"""
        channel = Channel(id_channel=id_channel)
        result = Channel.get(channel)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        """Get all channels"""
        channel_objects = Channel.get_all()
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200

    @classmethod
    def get_channels(cls, id_server):
        """Get all servers referidos a un ID de usuario"""
        channel = Channel(id_server=id_server)
        results = Channel.get_channels(channel)
        channels = []
        for channel in results:
            channels.append(channel.serialize())
        return channels, 200
    
    @classmethod
    def create(cls):
        """Create a new channel"""
        data = request.json
        
        channel = Channel(**data)
        Channel.create(channel)
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def update(cls, id_channel):
        """Update a channel"""
        data = request.json
        
        data['id_channel'] = id_channel

        channel = Channel(**data)
        
        Channel.update(channel)
        
        return {'message': 'Channel updated successfully'}, 200
        
    @classmethod
    def delete(cls, id_channel):
        """Delete a channel"""
        channel = Channel(id_channel=id_channel)
        
        Channel.delete(channel)
        
        return {'message': 'Channel deleted successfully'}, 204