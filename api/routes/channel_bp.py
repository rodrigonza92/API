from flask import Blueprint

from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/', methods=['GET'])(ChannelController.get_all)
channel_bp.route('/<int:id_channel>', methods=['GET'])(ChannelController.get)
channel_bp.route('/added/<int:id_server>', methods=['GET'])(ChannelController.get_channels)
channel_bp.route('/', methods=['POST'])(ChannelController.create)
channel_bp.route('/<int:id_channel>', methods=['PUT'])(ChannelController.update)
channel_bp.route('/<int:id_channel>', methods=['DELETE'])(ChannelController.delete)