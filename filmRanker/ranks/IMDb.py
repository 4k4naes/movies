import requests
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError


movie_list = []

def get_data():
    with sync_playwright() as p:
        url = 'https://www.imdb.com/chart/top/?ref_=hm_nv_menu'

        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
                    locale="pl-PL",
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except PlaywrightTimeoutError:
            print("Nie udało odnalezc sie strony.")
            return None

        try:
            page.wait_for_selector("span.full-price", state="attached", timeout=20000)
        except PlaywrightTimeoutError:
            print("Nie znaleziono elementu.")
            return None

        spans = page.locator("span.full-price").all_inner_texts()
        price_raw = next((s for s in spans if "zł" in s), None)

        browser.close()



get_data()