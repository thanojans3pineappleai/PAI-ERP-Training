from playwright.sync_api import Page 
def test_login_page(page: Page): 
    page.goto("https://pai-erp-qa.pineappleai.cloud/login") 
    assert "PAI ERP" in page.title() 
    assert "PAI ERP" in page.title() 
