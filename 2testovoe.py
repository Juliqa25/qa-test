from playwright.sync_api import sync_playwright

def test_playwright_title():
    expected_text = "Playwright enables reliable end-to-end testing for modern web apps."

    with sync_playwright() as p:
        browsers = [
            p.chromium.launch(channel="chrome", headless=True),
            p.firefox.launch(headless=True)
        ]

        for browser in browsers:
            page = browser.new_page()
            page.goto("https://playwright.dev/")

            header = page.locator("h1.hero__title.heroTitle_ohkl")
            actual_text = header.inner_text().strip()

            assert actual_text == expected_text, (
                f"В {browser.browser_type.name} ожидалось: '{expected_text}', "
                f"но получили: '{actual_text}'"
            )

            print(f" Проверка прошла успешно в {browser.browser_type.name}")
            browser.close()

if __name__ == "__main__":
    test_playwright_title()

