from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    # 1. run the browser
    browser = p.chromium.launch(headless=True)
    
    # 2. make the context
    context = browser.new_content()
    
    # 3. make the page
    page = context.new_page()
    
    # 4. enter the link
    page.goto('https://practice.qabrains.com/')
    
    # 5. find the role ,and fill
    page.get_by_role('textbox', name='Email').fill('qa_testers@qabrains.com')
    page.get_by_role('textbox', name='Password').fill('Password123')
    
    # 6. find the button and click to submit
    page.get_by_role('button', name='Login').click()
    
    # 7. assert loggin success
    expect(page.get_by_role('button', name='Logout')).to_be_visible()

    browser.close()
