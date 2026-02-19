import pytest
from playwright.sync_api import expect
from src.pages.booking_page import BookingPage

def test_check_availability(turn_on):
    booking = BookingPage(turn_on)
    booking.to_bookingpage()
    booking.fill_date('12/11/2024', '13/11/2024')
    check = booking.check_avbl()
    expect(check).to_be_visible()
