from src.utilities.constants import BASE_URL_UI

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL_UI, wait_until='commit')
