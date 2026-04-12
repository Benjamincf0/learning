import time

from playwright.sync_api import sync_playwright
from tqdm import tqdm


def open_readme():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://github.com/Benjamincf0")
    time.sleep(1)
    for _ in tqdm(range(1000)):
        page.reload()
        time.sleep(0.1)
    browser.close()

    playwright.stop()


def main():
    print("Hello from readme-hacker!")
    open_readme()


if __name__ == "__main__":
    main()
