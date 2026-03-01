import pytest
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()
BASE_URL_API = os.getenv('BASE_URL_API')
""" manage logging """

@pytest.fixture(scope="session", autouse=True)
def manage_logging():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    log_file = f'logs/run_{datetime.now().strftime("%y%m%d_%H%M%S")}.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(log_file)],
                        force=True
                        )


logger = logging.getLogger(__name__) # Mengambil logger yang sudah di-config

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Kita hanya mencatat saat test GAGAL di tahap eksekusi (call)
    if report.failed:
        is_ui = "ui_test" in item.nodeid
        page = item.funcargs.get("page") if is_ui else None
        logger.info(f'page {page}')
        test_name = item.name
        summary = str(report.longrepr.reprcrash.message) if hasattr(report.longrepr, 'reprcrash')  else "Error not defined"
        
        # Log ke file via logging module (Fixture kamu yang handle filenya)
        logger.error(f"TEST FAILED: {test_name}")
        logger.error(f"Short error Message: {summary}")

        if page and is_ui:
            # 1. Catat URL terakhir saat error
            logger.info(f"URL saat error: {page.url}")

            # 2. Tangkap Console Logs dari Browser (Sangat penting buat client-side exception)
            # Ini akan masuk ke file log yang sama
            logger.info("--- Browser Console Logs ---")
            # Log ini bisa kita ambil dari properti page jika kita setup listener (lihat poin 3)

            # 3. Ambil Screenshot untuk bukti visual
            if not os.path.exists('logs/screenshots'):
                os.mkdir('logs/screenshots')
            screenshot_path = f"logs/screenshots/fail_{test_name}_{datetime.now().strftime("%y%m%d_%H%M%S")}.png"
            page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot disimpan di: {screenshot_path}")

@pytest.fixture(autouse=True)
def capture_browser_console(page):
    # Callback untuk setiap pesan di console browser
    def handle_console(msg):
        if msg.type == "error":
            logger.error(f"BROWSER CONSOLE ERROR: {msg.text}")
        else:
            logger.info(f"BROWSER CONSOLE {msg.type.upper()}: {msg.text}")

    page.on("console", handle_console)
    yield

""" fixture for ui testing """
    
@pytest.fixture()
def browser_page(page):
    logger.info('>>>START')
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(15000)
    yield page
    logger.info('END<<<\n')
    
""" fixture for api testing """
                
@pytest.fixture(scope="session")
def token(playwright):
    headers = {
        "Accept" : "application/vnd.github.v3+json",
        }
    data = {
        "username" : "admin",
        "password" : "password123"
}
    p = playwright.request.new_context(base_url=BASE_URL_API, extra_http_headers=headers)
    response = p.post('/auth', data=data)
    r = response.json()
    assert r.get('token')
    yield r.get('token')
    p.dispose()
    
@pytest.fixture()
def api_request(playwright, token):
    logger.info('>>>START')
    headers = {
        "Accept" : "application/vnd.github.v3+json",
        "Cookie" : f"token={token}"
    }
    p = playwright.request.new_context(base_url = BASE_URL_API, extra_http_headers=headers)
    yield p
    logger.info('END<<<\n')
    p.dispose()
