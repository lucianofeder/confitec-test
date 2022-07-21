from behave import use_fixture
from tests.integration.helpers.app_instance import app_instance


def before_all(context):
    context.app = use_fixture(app_instance, context)
