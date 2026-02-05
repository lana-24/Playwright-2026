from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://practice.qabrains.com/forgot-password')

    page.get_by_role('textbox', name='Email').fill('user@user.com')
    
    page.get_by_role('button', name='Reset Password').click()
    
    expect(page.get_by_text('Password is reset successfully.')).to_be_visible()

    browser.close()
