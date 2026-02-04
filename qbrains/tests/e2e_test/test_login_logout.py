from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    # 1.run the browser
    browser = p.chromium.launch(headless=True)
    # 2.make the context
    context = browser.new_context()
    # 3.make the page
    page = context.new_page()
    # 4.visit to https://practice.qabrains.com/ecommerce/login
    page.goto('https://practice.qabrains.com/ecommerce/login')
    # 5.fill Email
    page.get_by_role('textbox', name='Email').fill('test@qabrains.com')
    # 6.fill Password
    page.get_by_role('textbox', name='Password').fill('Password123')
    # 7.click the button 
    page.get_by_role('button', name='Login').click()
    # 8.assert login succesfully 
    expect(page.get_by_text('Products')).to_be_visible()
    # 9.click profile
    page.get_by_role('button', name='test@qabrains.com').click()
    # 10.click logout
    page.get_by_role('button', name='Log out').click()
    # 11.click yes
    page.get_by_role('button', name='Logout').click()
    # 12.assert logout sucesfully
    expect(page.get_by_role('button', name='Login')).to_be_visible()
