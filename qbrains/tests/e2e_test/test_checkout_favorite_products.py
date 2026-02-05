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

    # 9.add products to favorite list
    products = ['Sample Shoe Name',
                'Sample Shirt Name',
                'Sample Trouser Name']
    for p in products:
        product = page.locator('div.flex.flex-col.gap-3', has_text=p)
        product.locator("span[role='button']").click()
    # 10.click favorite list
    page.get_by_role('button', name='test@qabrains.com').click()
    page.get_by_role("menuitem", name="Favorite").click()
    # 11.add to cart
    for product in products:
        page.locator('div.flex.flex-col.gap-3', has_text=product).get_by_role('button', name='Add to cart').click()
    # 11.click cart
    page.locator('span[role="button"].relative').click()
    # 12.click checkout and fill form
    page.get_by_role('button', name='Checkout').click()
    page.get_by_placeholder('Ex. John').fill('mal')
    page.get_by_placeholder('Ex. Doe').fill('ik')
    # 13.click continue
    page.get_by_role('button', name='Continue').click()
    # 14.click Finish
    page.get_by_role('button', name='Finish').click()
    # 15. assert checkout success
    expect(page.get_by_role('button', name='Continue Shopping')).to_be_visible()
    # 16.log out
    page.get_by_role('button', name='test@qabrains.com').click()
    page.get_by_role('button', name='Log out').click()
    page.get_by_role('button', name='Logout').click()
    expect(page.get_by_role('button', name='Login')).to_be_visible()

    browser.close()
