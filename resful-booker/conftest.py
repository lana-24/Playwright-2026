import pytest
import os
from datetime import datetime
import logging
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def manage_logging():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    log_file = f'logs/run_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(log_file)],
                        force=True
                        )


@pytest.fixture()
def turn_on():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()  
