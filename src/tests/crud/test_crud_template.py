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
    def test_update_bookingid_token(self):
        pass

    def test_delete_booking_id(self):
        pass
