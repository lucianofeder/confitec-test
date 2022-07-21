from app.controllers.artist_controller import ArtistController
from flask import Blueprint, request

artist_bp = Blueprint('Artist', __name__)

controller = ArtistController()


@artist_bp.route('/search')
def search():
    return controller.search(**request.args)
