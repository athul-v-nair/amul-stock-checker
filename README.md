# Amul Protein Lassi Stock Checker

A Python automation tool to check the stock availability of **Amul High
Protein Lassi** products on the Amul online store and notify the user
via WhatsApp when the product is in stock.

------------------------------------------------------------------------

## Features

-   Checks stock for:
    -   **Amul High Protein Rose Lassi**
    -   **Amul High Protein Plain Lassi**
-   Pincode-based location selection.
-   Sends notifications via WhatsApp using Twilio.
-   Maintains previous stock state to notify only on changes.
-   Lightweight, asynchronous, and easy to run locally.

------------------------------------------------------------------------

## System Design (Simplified)

     +---------------------+
     |      main.py        |  <-- Entry point
     +---------------------+
               |
               v
     +---------------------+
     |   store_checker.py  |  <-- Playwright logic
     | - Set pincode       |
     | - Scrape products   |
     | - Detect stock      |
     +---------------------+
               |
               v
     +---------------------+
     |    DOMinjection.py  |  <-- DOM utilities
     +---------------------+
               |
               v
     +---------------------+
     |    notifier.py      |  <-- Sends WhatsApp notifications
     +---------------------+
               |
               v
           User Device

------------------------------------------------------------------------

## File Descriptions

-   **config.py** --- contains product names and pincode.\
-   **notifier.py** --- uses Twilio WhatsApp sandbox to send
    notifications.\
-   **store_checker.py** --- contains the scraping logic using
    Playwright.\
-   **DOMinjection.py** --- helper functions to interact with page
    elements.

------------------------------------------------------------------------

## Requirements

-   Python 3.10+
-   Playwright
-   python-dotenv
-   Twilio SDK

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/amul-lassi-checker.git
cd amul-lassi-checker
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

``` bash
python -m playwright install
```

### 4. Create `.env` file

Create a `.env` file in the root directory:

    # Twilio WhatsApp
    TWILIO_SID=your_twilio_sid
    TWILIO_TOKEN=your_twilio_auth_token
    TWILIO_FROM=whatsapp:+1415523XXXX   # Twilio WhatsApp sandbox number
    WHATSAPP_TO=whatsapp:+91XXXXXXXXXX  # Your number

    # Pincode to check
    PINCODE=683511

Replace placeholders with your Twilio sandbox credentials and your
pincode.

------------------------------------------------------------------------

### 5. Run the script locally

``` bash
python main.py
```

### Script actions:

-   Opens the Amul store page using Playwright.
-   Enters the pincode.
-   Checks for stock of the two lassi products.
-   Sends a WhatsApp message if any product is in stock (state changes
    are tracked to avoid duplicate notifications).

------------------------------------------------------------------------

## Project Structure

    scraper/
    │
    ├─ config.py         # Product list and pincode
    ├─ DOMinjection.py   # DOM helper functions
    ├─ notifier.py       # WhatsApp notification module
    ├─ store_checker.py  # Playwright scraping logic
    │
    .gitignore
    main.py              # Entry point
    requirements.txt

## Contributions

-   Contributions are welcome! If you'd like to improve the scraper, fix bugs, or add new features please free to do so.