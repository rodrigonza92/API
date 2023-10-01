from flask import Blueprint

from ..controllers.message_controller import MessageController

message_bp = Blueprint('message_bp', __name__)

message_bp.route('/', methods=['GET'])(MessageController.get_all)
message_bp.route('/<int:id_channel>', methods=['GET'])(MessageController.get)
message_bp.route('/', methods=['POST'])(MessageController.create)
message_bp.route('/<int:id_message>', methods=['PUT'])(MessageController.update)
message_bp.route('/<int:id_message>', methods=['DELETE'])(MessageController.delete)