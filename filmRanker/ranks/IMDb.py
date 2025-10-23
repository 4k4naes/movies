from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def get_dataI():
    with sync_playwright() as p:
        url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36"
            ),
            locale="pl-PL",
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except PlaywrightTimeoutError:
            print("Nie udało się załadować strony.")
            return None

        try:
            page.wait_for_selector("li.ipc-metadata-list-summary-item h3.ipc-title__text", state="attached", timeout=20000)
        except PlaywrightTimeoutError:
            print("Nie znaleziono elementu z tytułami filmów.")
            return None

        titles = page.locator("li.ipc-metadata-list-summary-item h3.ipc-title__text").all_inner_texts()

        for t in titles:
            print(t)

        browser.close()
