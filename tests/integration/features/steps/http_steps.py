from behave import * #  noqa: F405,F403


@step(u'the response code should be "{response_code}"')
def check_response_status_code(context, response_code):
    assert context.request_response.status_code == int(response_code)


@step(u'I send a "{http_method}" request to "{api_route}"')
def send_request(context, http_method, api_route):
    https_map = {
        "get": context.app.get,
    }
    context.request_response = https_map[http_method](api_route)


@then(u'the "{key}" key in the response should have an array with length "{length}"')
def check_length_arrays_in_response(context, key, length):
    assert len(context.request_response.json[key]) == int(length)


@step(u'the response "{key}" key should be "{value}"')
def check_response_key_value(context, key, value):
    assert context.request_response.json[key] == value
