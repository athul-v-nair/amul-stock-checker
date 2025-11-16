import asyncio
from scraper.store_checker import check_stock,load_state,save_state
from scraper.notifier import notify_whatsapp

async def main():
    last_state = load_state()
    current_state = await check_stock()

    print("LAST STATE:", last_state)
    print("CURRENT STATE:", current_state)

    notifications = []

    for product, status in current_state.items():
        # default OUT when no previous data exists
        last_status = last_state.get(product, "OUT")  
        
        if last_status == "OUT" and status == "IN":
            notifications.append(product)

    # Update state file
    save_state(current_state)

    # If nothing became available
    if not notifications:
        print("No new IN STOCK items.")
        return

    # Build readable message
    msg = "🟢 **New items IN STOCK!**\n\n" + "\n".join(f"- {p}" for p in notifications)

    # Send single combined notification
    notify_whatsapp(msg)

    print("Notification sent for:", notifications)

if __name__=="__main__":
    asyncio.run(main())