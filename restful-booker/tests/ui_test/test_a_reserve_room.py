import pytest
import logging
from playwright.sync_api import expect
from src.pages.select_room import BookRoom
from test_data.fill_users import valid_users, invalid_users, invalid_firstname, invalid_lastname, invalid_email, invalid_phone 

logger = logging.getLogger(__name__)

#@pytest.mark.parametrize('fname, lname, email, phone', valid_users)
@pytest.mark.parametrize('fname, lname, email, phone',
                         valid_users
                         #[('lana','lako','lana@test.com','1121212123123')]
                         )
def test_booking_rooms(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    response_value = booking.submit_valid_form()
    if response_value.status >= 400:
        logger.error(f'status code {response_value.status}, response: {response_value.json()}')
        pytest.fail(f'status code {response_value.status}, response: {response_value.json()}')
        
    return_home = booking.return_home()
    expect(return_home).to_be_attached()
    logger.info('Booking Confirmed')
    return_home.click(force=True)

#@pytest.mark.parametrize('fname, lname, email, phone', invalid_users)
@pytest.mark.parametrize('fname, lname, email, phone',
                         invalid_users
                         #[('la','li','lanatest.com','1121')]
                         )
def test_booking_with_invalid_identity(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert isinstance(list_error, list)
    expected = ['size must be between 3 and 30',
                'size must be between 11 and 21',
                'size must be between 3 and 18',
                'must be a well-formed email address']
    assert sorted(list_error) == sorted(expected)

#@pytest.mark.parametrize('fname, lname, email, phone', invalid_firstname)
@pytest.mark.parametrize('fname, lname, email, phone',
                         invalid_firstname
                         #[('la','lano','lana@test.com','1121212123123')]
                         )
def test_booking_with_invalid_fname(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert isinstance(list_error, list)
    expected = ['size must be between 3 and 18']
    assert list_error == expected

#@pytest.mark.parametrize('fname, lname, email, phone', invalid_lastname)
@pytest.mark.parametrize('fname, lname, email, phone',
                         invalid_lastname
                         #[('lana','la','lana@test.com','1121212123123')]
                         )
def test_booking_with_invalid_lname(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert isinstance(list_error, list)
    expected = ['size must be between 3 and 30']
    assert list_error == expected

#@pytest.mark.parametrize('fname, lname, email, phone', invalid_email)
@pytest.mark.parametrize('fname, lname, email, phone',
                         invalid_email
                         #[('lana','lano','lanatest.com','1121212123123')]
                         )
def test_booking_with_invalid_email(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert isinstance(list_error, list)
    expected = ['must be a well-formed email address']
    assert list_error == expected

#@pytest.mark.parametrize('fname, lname, email, phone', invalid_phone)
@pytest.mark.parametrize('fname, lname, email, phone',
                         invalid_phone
                         #[('lana','lano','lana@test.com','112123')]
                         )
def test_booking_with_invalid_phone(browser_page, fname, lname, email, phone):
    booking = BookRoom(browser_page)
    booking.to_rooms()
    room = booking.select_room()
    assert room is True
    booking.reserve_room(fname, lname, email, phone)
    list_error = booking.submit_invalid_form()
    assert isinstance(list_error, list)
    expected = ['size must be between 11 and 21']
    assert list_error == expected

