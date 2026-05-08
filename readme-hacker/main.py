import sys
import time

from playwright.sync_api import sync_playwright
from tqdm import tqdm


def open_readme(numReloads: int) -> None:
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://github.com/Benjamincf0")
    time.sleep(1)
    for _ in tqdm(range(numReloads)):
        page.reload()
        time.sleep(0.1)
    browser.close()

    playwright.stop()


def main(args: list[str]) -> int:
    print("Hello from readme-hacker!")
    if len(args) < 2:
        print(f"Usage: python {args[0]} <num-reloads>")
        return 1

    try:
        int(args[1])
    except ValueError:
        print(f"Usage: python {args[0]} <num-reloads>")
        return 2

    open_readme(int(args[1]))
    return 0


if __name__ == "__main__":
    main(sys.argv[:])
