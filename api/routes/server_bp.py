from flask import Blueprint

from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/', methods=['GET'])(ServerController.get_all)
server_bp.route('/<int:id_server>', methods=['GET'])(ServerController.get)
server_bp.route('/', methods=['POST'])(ServerController.create)
server_bp.route('/<int:id_server>', methods=['PUT'])(ServerController.update)
server_bp.route('/<int:id_server>', methods=['DELETE'])(ServerController.delete)