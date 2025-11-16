import asyncio
from scraper.store_checker import check_stock,load_state,save_state
from scraper.notifier import notify_whatsapp

async def main():
    previous_state=load_state()["last_status"]
    
    current_state=await check_stock()
    
    if previous_state=="OUT" and current_state=="IN":
        message="Protien Lassi is in stock!!"
        notify_whatsapp(message)
        
    save_state(current_state)
    
if __name__=="__main__":
    asyncio.run(main())