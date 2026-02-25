import pytest
from playwright.sync_api import expect
from src.pages.booking_page import BookingPage
import logging 

logger = logging.getLogger(__name__)

def test_check_availability(page):
    booking = BookingPage(page)
    logger.info('open web')
    booking.to_bookingpage()
    booking.fill_date('12/11/2024', '13/11/2024')
    check = booking.check_avbl()
    expect(check).to_be_visible()
