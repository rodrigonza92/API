from ..models.message_model import Message

from flask import request

class MessageController:
    
    @classmethod
    def get(cls, id_message):
        """Get a channel by id"""
        channel = Message(id_message=id_message)
        result = Message.get(channel)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        """Get all channels"""
        channel_objects = Message.get_all()
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200

    @classmethod
    def create(cls):
        """Create a new channel"""
        data = request.json
        
        channel = Message(**data)
        Message.create(channel)
        return {'message': 'Message created successfully'}, 201

    @classmethod
    def update(cls, id_message):
        """Update a channel"""
        data = request.json
        
        data['id_message'] = id_message

        channel = Message(**data)
        
        Message.update(channel)
        
        return {'message': 'Message updated successfully'}, 200
        
    @classmethod
    def delete(cls, id_message):
        """Delete a channel"""
        channel = Message(id_message=id_message)
        
        Message.delete(channel)
        
        return {'message': 'Message deleted successfully'}, 204