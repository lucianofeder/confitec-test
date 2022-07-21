from behave import fixture

from app import create_app


@fixture
def app_instance(*args, **kwargs):
    app = create_app()
    app.app_context().push()
    yield app.test_client()
