import pytest
import logging
from playwright.sync_api import expect
from src.pages.select_room import BookRoom
from test_data.fill_users import valid_users, invalid_users, invalid_firstname, invalid_lastname, invalid_email, invalid_phone 

logger = logging.getLogger(__name__)

@pytest.mark.parametrize('fname, lname, email, phone', valid_users)
def test_booking_rooms(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    confirmed = booking.submit_valid_form()
    expect(confirmed).has_to_visible()
    logger.info('Booking Confirmed')

@pytest.mark.parametrize('fname, lname, email, phone', invalid_users)
def test_booking_with_invalid_identity(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert list_error is list
    expected = ['size must be between 3 and 30',
                'size must be between 11 and 21',
                'size must be between 3 and 18',
                'must be a well-formed email address']
    assert sorted(list_error) == sorted(expected)

@pytest.mark.parametrize('fname, lname, email, phone', invalid_firstname)
def test_booking_with_invalid_fname(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert list_error is list
    expected = ['size must be between 3 and 18']
    assert list_error == expected

@pytest.mark.parametrize('fname, lname, email, phone', invalid_lastname)
def test_booking_with_invalid_lname(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert list_error is list
    expected = ['size must be between 3 and 30']
    assert list_error == expected

@pytest.mark.parametrize('fname, lname, email, phone', invalid_email)
def test_booking_with_invalid_email(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert list_error is list
    expected = ['must be a well-formed email address']
    assert list_error == expected

@pytest.mark.parametrize('fname, lname, email, phone', invalid_phone)
def test_booking_with_invalid_phone(turn_on, fname, lname, email, phone):
    booking = BookRoom(turn_on)
    booking.to_rooms()
    booking.select_room('single')
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert list_error is list
    expected = ['size must be between 11 and 21']
    assert list_error == expected
