from src.pages.base_page import BasePage

class RoomsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page.locator('.navbar-toggler').click()
        self.page.locator('#navbarNav').get_by_role('link', name='Rooms')
        
