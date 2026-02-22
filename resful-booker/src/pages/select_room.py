import logging
from playwright.sync_api import expect
from src.pages.base_page import BasePage
from typing import Literal

logger = logging.getLogger(__name__)

class BookRoom(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def to_rooms(self):
        self.navigate()
        self.page.locator('.navbar-toggler').dispatch_event('click')
        self.page.locator('#navbarNav').get_by_role('link', name='Rooms').click()
        self.page.get_by_role('button', name='Check Availability').click()

    def select_room(self):
        for o in ['single', 'double', 'suite']:
            logger.info(f'select {o} room')
            room = self.page.locator('.card').filter(has_text=o).get_by_role('link', name='Book now')
            if room.is_visible(timeout=2000):
                room.click()
                return True
            else:
                logger.info(f"{o} room is not visible")

    def reserve_room(self, fname: str, lname: str, email: str, phone: int):
        self.page.get_by_role('button', name='Reserve Now').click()
        logger.info(f'try booking with the name {fname}')
        # fill first name
        logger.info(f'fill firstname: {fname}')
        self. page.get_by_label('Firstname').fill(fname)
        # fill last name
        logger.info(f'fill lastname: {lname}')
        self.page.get_by_label('Lastname').fill(lname)
        # fill email
        logger.info(f'fill email: {email}')
        self.page.get_by_label('Email').fill(email)
        # fill phone num
        logger.info(f'fill phone: {phone}')
        self.page.get_by_label('Phone').fill(phone)

    def submit_valid_form(self):
        logger.info('click reserve now')
        with self.page.expect_response('**/api/booking') as response_info:
            self.page.get_by_role('button', name='Reserve Now').click()
            
        self.response = response_info.value
        return self.page.locator('a:has-text("Return home")')

    def get_id(self):
        logger.debug('getting booking id')
        return self.response.json().get('bookingid')

    def submit_invalid_form(self):
        self.page.get_by_role('button', name='Reserve Now').click()
        self.page.locator('.alert-danger li').first.wait_for()
        list_error = self.page.locator('.alert-danger li').all_inner_texts()
        logger.info(f'an error warning appears, total: {len(list_error)}')
        return list_error
    
