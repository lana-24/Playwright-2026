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

    # 9.add some product to cart
    products = ['Sample Shoe Name',
                'Sample Shirt Name',
                'Sample Trouser Name']
    for product in products:
        page.locator('div.flex.flex-col.gap-3', has_text=product).get_by_role('button', name='Add to cart').click()
    # 10.click cart
    page.locator('span[role="button"].relative').click()
    # 11.remove all products in cart
    for product in products:
        page.locator('div.flex.items-center.gap-5', has_text=product).get_by_role('button', name='Remove').click()
        page.get_by_role('button', name='Remove').click()

    # 12.click profile
    page.get_by_role('button', name='test@qabrains.com').click()
    # 13.click logout
    page.get_by_role('button', name='Log out').click()
    # 14.click yes
    page.get_by_role('button', name='Logout').click()
    # 15.assert logout sucesfully
    expect(page.get_by_role('button', name='Login')).to_be_visible()

    browser.close()
