import os
import json
from playwright.async_api import async_playwright
from scraper.config import PRODUCT_URL,PRODUCT_NAMES,STATE_FILE
from scraper.DOMinjection import apply_pincode

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)
        
async def check_stock():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
        page=await browser.new_page()
        
        # Redirect to product url
        await page.goto(PRODUCT_URL, timeout=60000)
        await page.wait_for_timeout(2000)
        
        # Adding the Pin code
        await apply_pincode(page)
        
        # Wait for product catalouge to load
        await page.wait_for_selector("div.product-list-items", timeout=60000)

        results = {}

        for product in PRODUCT_NAMES:
            # Find all elements containing the product name
            product_elements = await page.query_selector_all(f":text('{product}')")

            if not product_elements:
                print(f"[NOT FOUND] {product}")
                results[product] = "NOT_FOUND"
                continue
            
            for el in product_elements:
                is_out_of_stock = await el.evaluate(
                    """(node) => {
                        let parent = node.parentElement;
                        while (parent) {
                            if (parent.classList.contains('outofstock')) return true;
                            parent = parent.parentElement;
                        }
                        return false;
                    }"""
                )

            if is_out_of_stock:
                results[product]="OUT"
            else: 
                results[product]="IN"

    return results