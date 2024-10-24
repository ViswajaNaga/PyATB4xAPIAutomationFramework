# API TestCase

# URL -> API_Constants.py
# headers -> Utils.py
# payload -> payload_manager.py
# HTTP POST -> api_request_wrapper.py
# verification -> common_verification.py
# object class is the father of all the classes....
# so given object while creating a class - Single inheritance.
# even if we don't give it doesn't make a difference

import pytest
import allure

class TestCreateBooking(object):

    def test_create_booking_positive(self):
        pass

    def test_create_booking_negative(self):
        pass
