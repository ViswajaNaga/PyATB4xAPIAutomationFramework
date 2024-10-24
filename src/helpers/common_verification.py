# common verification
# HTTP status code
# Headers
# Data verification
# JSON Schema Verification

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed Status Code Match"


def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_json_key_for_not_null(key):
    assert key != 0, "Failed-Key is equal to zero"
    assert key > 0, "Failed- Key is not greater than zero" + key


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed-Key is non empty" + key


def verify_response_delete(response):
    assert "Created" in response