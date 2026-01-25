from urllib.parse import urljoin
from playwright.sync_api import expect

def test_jobs_opens_careers(setup_playwright):
    page = setup_playwright

    page.goto("https://wolt.com/en/isr", wait_until="domcontentloaded")
    for name in ["Accept all", "Allow", "Accept"]:
        btn = page.get_by_role("button", name=name)
        if btn.count() > 0 and btn.first.is_visible():
            btn.first.click()
            break
    jobs = page.get_by_role("link", name="Jobs")
    expect(jobs).to_be_visible(timeout=15000)
    href = jobs.get_attribute("href")
    full_url = urljoin(page.url, href)
    page.goto(full_url, wait_until="domcontentloaded")
    import re
    expect(page).to_have_url(re.compile(r".*careers\.wolt\.com.*"), timeout=15000)

