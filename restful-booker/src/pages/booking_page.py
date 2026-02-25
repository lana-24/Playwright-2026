from src.pages.base_page import BasePage
import logging

logger =  logging.getLogger(__name__)

class BookingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def to_bookingpage(self):
        logger.info('click navigate')
        self.navigate()
        self.page.locator('.navbar-toggler').dispatch_event('click')
        self.page.locator('#navbarNav').get_by_role('link', name='Booking').click()
        
    def fill_date(self, ckin, ckout):
        checkin = self.page.locator("xpath=//label[@for='checkin']/following-sibling::div//input")
        checkout = self.page.locator("xpath=//label[@for='checkout']/following-sibling::div//input")
        logger.info(f'fill checkin date {ckin}')
        checkin.fill(ckin)
        logger.info(f'fill checkin date {ckout}')
        checkout.fill(ckout)

    def check_avbl(self):
        logger.info('check available room')
        self.page.get_by_role('button', name='Check Availability').click()
        return self.page.get_by_role('heading', name='Our Rooms')
