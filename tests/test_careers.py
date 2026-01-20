from playwright.sync_api import expect

def test_jobs_opens_careers(setup_playwright):
    page = setup_playwright

    with page.expect_popup() as popup_info:
        page.get_by_role("menuitem", name="Jobs").click()

    careers_tab = popup_info.value

    h1 = careers_tab.locator("h1.text-white.my-0")
    expect(h1).to_be_visible(timeout=15000)
    expect(h1).to_have_text("the ride of your life", timeout=15000)
