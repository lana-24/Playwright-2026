from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://practice.qabrains.com/registration')

    #1. fill name
    page.get_by_role('textbox', name='Name').fill('Jhon Doe')

    #2. select country
    page.get_by_role('combobox', name='Select Country').select_option('Indonesia')

    #3. select account type
    page.get_by_role('combobox', name='Account Type').select_option('Engineer')

    #4. fill email
    page.get_by_role('textbox', name='Email').fill('user@user.com')

    #5. fill password and confirm password
    page.locator('#password').fill("Password123")
    page.get_by_role('textbox', name='Confirm Password').fill('Password123')

    #6. click button
    page.get_by_role('button', name='Signup').click()

    #7. assert registration success
    expect(page.get_by_role('button', name='Login')).to_be_visible()

    browser.close()
    
