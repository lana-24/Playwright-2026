import logging
import pytest
from playwright.sync_api import expect
from src.pages.base_page import BasePage
from typing import Literal
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class BookRoom(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def to_rooms(self):
        self.navigate()
        tommorow  = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.page.locator("xpath=//label[@for='checkin']/following-sibling::div//input").fill(datetime.now().strftime("%d/%m/%Y"))
        logger.info(f'fill chekin: {datetime.now().strftime("%d/%m/%Y")}')
        self.page.locator("xpath=//label[@for='checkout']/following-sibling::div//input").fill(tommorow)
        logger.info(f'fill chekin: {tommorow}')
        self.page.get_by_role('button', name='Check Availability').dispatch_event('click')
        self.page.wait_for_load_state("networkidle")
        logger.info('check available done')

    def select_room(self):
        for o in ['single', 'double', 'suite']:
            room = self.page.locator('.card').filter(
            has=self.page.locator('.card-title', has_text=o)
            ).get_by_role('link', name='Book now')

            if room.is_visible(timeout=5000):
                logger.info(f'select {o} room')
                room.wait_for(state="attached", timeout=5000)
                room.click(force=True)
                return True
            
        logger.error("all room is not visible")
        return False

    def reserve_room(self, fname: str, lname: str, email: str, phone: int):
        self.page.get_by_role('button', name='Reserve Now').dispatch_event('click')
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
            self.page.get_by_role('button', name='Reserve Now').dispatch_event('click')
            #self.page.locator('.btn-secondary').filter(has_text='Reserve Now').click()
        self.response = response_info.value
        self.response_code = self.response.status 
        if self.response_code == 409:
            logger.error(f"{self.response_code}: {self.response.json().get('error')}, your resource might be duplicate.")
            pytest.fail('Application error')
        return self.response
        
    def return_home(self):
        return self.page.locator('a').filter(has_text="Return home")

    def get_id(self):
        logger.debug('getting booking id')
        return self.response.json().get('bookingid')

    def submit_invalid_form(self):
        self.page.get_by_role('button', name='Reserve Now').click()
        self.page.locator('.alert-danger li').first.wait_for()
        list_error = self.page.locator('.alert-danger li').all_inner_texts()
        logger.info(f'an error warning appears, total: {len(list_error)}')
        return list_error
    
