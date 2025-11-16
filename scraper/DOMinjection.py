from playwright.async_api import Page
from scraper.config import PINCODE

async def apply_pincode(page: Page):
    print("Entering pincode: ",PINCODE)
    await page.fill("div.input-auto-substore input", PINCODE)
    
    await page.wait_for_selector("#automatic .searchitem-name")
    
    await page.click("#automatic .searchitem-name")
    
    await page.wait_for_timeout(5000)