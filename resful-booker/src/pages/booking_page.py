from src.pages.base_page import BasePage

class BookingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def to_bookingpage(self):
        self.navigate()
        self.page.locator('.navbar-toggler').click()
        self.page.locator('#navbarNav').get_by_role('link', name='Booking').click()
        
    def fill_date(self, ckin, ckout):
        checkin = self.page.locator("xpath=//label[@for='checkin']/following-sibling::div//input")
        checkout = self.page.locator("xpath=//label[@for='checkout']/following-sibling::div//input")
        checkin.fill(ckin)
        checkout.fill(ckout)

    def check_avbl(self):
        self.page.get_by_role('button', name='Check Availability').click()
        return self.page.get_by_role('heading', name='Our Rooms')
