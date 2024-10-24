# API TestCase

# URL -> API_Constants.py
# headers -> Utils.py
# payload -> payload_manager.py
# HTTP POST -> api_request_wrapper.py
# verification -> common_verification.py

import pytest
import allure
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging

class Test_Create_Booking(object):
    @pytest.mark.positive
    @allure.title("Verify the create booking status and Booking ID shouldn't be null")
    @allure.description("Create a booking from the payload and bookingId should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the testcase TC1-Positive")
        post_response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=post_response, expected_data=200)
        verify_json_key_for_not_null(post_response.json()["bookingid"])
        LOGGER.info(post_response.json()["bookingid"])
        LOGGER.info("End of the testcase TC1-Positive")

    @pytest.mark.negative
    @allure.title("Verify that create booking doesn't work with no payload")
    @allure.description("Create a booking with no payload and verify that bookingId")
    def test_create_booking_negative(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the testcase TC2-Negative")
        post_response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=post_response,expected_data=500)


