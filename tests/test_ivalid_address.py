from playwright.sync_api import expect

def test_invalid_addresses(setup_playwright):
    page = setup_playwright
    page.goto("https://wolt.com/en/isr", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    for name in ["Accept all", "Allow", "Accept"]:
        btn = page.get_by_role("button", name=name)
        if btn.count() > 0 and btn.first.is_visible():
            btn.first.click()
            break

    search = page.get_by_placeholder("Enter delivery address")
    expect(search).to_be_visible(timeout=60_000)
    search.click()
    search.fill("ghghghghghghgh")

    expect(page.get_by_text("No addresses found")).to_be_visible(timeout=15_000)
