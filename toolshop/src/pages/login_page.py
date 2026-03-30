from base_page import BasePage

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navigate()
        self.menu_button = "button[aria-label='Toggle navigation']"
        
    def fill_form(self, email=None, password=None):
        self.page.click(self.menu_button)
        self.page.get_by_role("link", name="Sign in").click()

        if email:
            self.page.get_by_test_id("email").fill(email)
        else:
            self.page.get_by_test_id("email").focus()

        if password:
            self.page.get_by_test_id("password").fill(password)
        else:
            self.page.get_by_test_id("password").focus()

        self.page.get_by_test_id("login-submit").click()
        
    def click_logout(self):
        # click menu button
        self.page.click(self.menu_button)
        # click account
        self.page.get_by_role("link", name="Bob Smith").click()
        # click sign out
        self.page.get_by_role("link", name="Sign out").click()
