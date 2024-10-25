# Conftest

# Create Token
# create bookingid
# update the booking(PUT) -BookingId and token
# delete the booking

# Verify that created booking id when we update, we are able to update it and delete it

from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils
import pytest
import allure




class TestCRUDBooking(object):
    @allure.title("Test CRUD Operation Update(PUT")
    @allure.description("Verify the Full update with the Valid BookingId and Token")
    def test_update_booking_id_token(self,create_token,get_booking_id):

        put_url=APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        response = put_request(
            url=put_url,
            auth=None,
            headers=Utils().common_header_put_patch_delete_cookie(token=create_token),
            payload=payload_update_booking(),
            in_json=False
        )
        # Verification here and more
        verify_response_key(response.json()["firstname"],expected_data="Amit")
        verify_response_key(response.json()["lastname"], expected_data="Brown")
        verify_http_status_code(response_data=response,expected_data=200)


    def test_delete_booking_id(self,create_token,get_booking_id):
        delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_header_put_patch_delete_cookie(token=create_token),
            in_json=False
        )
        verify_response_delete(response=response.text)
        print(response.text)
        verify_http_status_code(response_data=response,expected_data=201)