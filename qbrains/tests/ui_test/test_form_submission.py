from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://practice.qabrains.com/form-submission')

    page.get_by_role('textbox', name='Name').fill('Jhon Doe')
    page.get_by_role('textbox', name='Email').fill('user@user.com')
    page.get_by_role('textbox', name='Contact Number').fill('0312381231231')
    page.get_by_label("Date").fill("2026-02-03")
    page.get_by_label("Upload File").set_input_files("path/ke/file/kamu.jpg")
    page.get_by_label("Green").check()
    page.get_by_label("Pasta").check()
    page.get_by_label("Burger").check()
    page.get_by_role('combobox', name='Select Country').select_option('Indonesia')
    page.locator("button.btn-submit").click()

    expect(page.get_by_text('Form submit successfully.')).to_be_visible()
