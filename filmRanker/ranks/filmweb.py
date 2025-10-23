from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

def get_dataF():
    with sync_playwright() as p:
        url = "https://www.filmweb.pl/ranking/film"

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
            return

        page.wait_for_selector("h2.rankingType__title", timeout=20000)

        last_height = 0
        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2) 
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        headers = page.locator("h2.rankingType__title")
        count = headers.count()

        for i in range(count):
            h2 = headers.nth(i)
            position = h2.locator("span.rankingType__position").inner_text()
            title = h2.locator("a[itemprop='url']").inner_text()
            print(f"{position} {title}")

        browser.close()