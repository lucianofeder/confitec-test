from flask import Flask


def init_app(app: Flask) -> None:
    from app.routes.artist_route import artist_bp
    app.register_blueprint(artist_bp, url_prefix='/artist')
