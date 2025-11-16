import os
from dotenv import load_dotenv
import json
from playwright.async_api import async_playwright
from scraper.config import product_url
from scraper.config import pincode
from scraper.DOMinjection import apply_pincode

load_dotenv()
STATE_FILE="state.json"
PRODUCT_NAME="Amul High Protein Rose Lassi"

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"last_status": "OUT"}
    
def save_state(status: str):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_status": status}, f)
        
async def check_stock():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
        page=await browser.new_page()
        await page.goto(os.getenv("PRODUCT_URL"), timeout=60000)
        await page.wait_for_timeout(2000)
        
        # Adding the Pin code
        await apply_pincode(page)
        
        # Wait for product catalouge to load
        await page.wait_for_selector("div.catalog-body, div.product-list-items", timeout=60000)
        
        # Look for the product
        product_elements=await page.query_selector_all(f"text='{PRODUCT_NAME}")
        
        if not product_elements:
            print("Product not found!")
            return "NOT_FOUND"
        
        for el in product_elements:
            # Check in parent if outofstock class is present
            parent= await el.evaluate_handle(
                """(node)=> {
                    let parent = node.parentElement;
                    while(parent){
                        if(parent.classList.contains('outofstock')) return true;
                        
                        parent = parent.parentElement;
                    }
                    return false;
                }
                """
            )
            
            if await parent.json_value():
                return "OUT"
            else:
                return "IN"
            
        return "UNKNOWN"