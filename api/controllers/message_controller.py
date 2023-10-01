from ..models.message_model import Message

from flask import request

class MessageController:
    
    @classmethod
    def get(cls, id_channel):
        """Get a message by id"""
        id = Message(id_channel=id_channel)
        result = Message.get(id)
        messages = []
        for message in result:
            messages.append(message.serialize())
        return messages, 200

    @classmethod
    def get_all(cls):
        """Get all messages"""
        message_objects = Message.get_all()
        messages = []
        for message in message_objects:
            messages.append(message.serialize())
        return messages, 200

    @classmethod
    def create(cls):
        """Create a new message"""
        data = request.json
        
        message = Message(**data)
        Message.create(message)
        return {'message': 'Message created successfully'}, 201

    @classmethod
    def update(cls, id_message):
        """Update a message"""
        data = request.json
        
        data['id_message'] = id_message

        message = Message(**data)
        
        Message.update(message)
        
        return {'message': 'Message updated successfully'}, 200
        
    @classmethod
    def delete(cls, id_message):
        """Delete a message"""
        message = Message(id_message=id_message)
        
        Message.delete(message)
        
        return {'message': 'Message deleted successfully'}, 204