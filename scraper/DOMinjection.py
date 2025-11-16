from playwright.async_api import Page
from scraper.config import pincode

async def apply_pincode(page: Page):
    print("Entering pincode: ",pincode)
    
    await page.fill("div.input-auto-substore input", pincode)
    
    await page.wait_for_selector("#automatic .searchitem-name")
    
    await page.click("#automatic .searchitem-name")
    
    await page.wait_for_timeout(5000)