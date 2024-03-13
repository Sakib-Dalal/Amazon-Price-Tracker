# Amazon Price Tracker

This is a simple Python script to track the price of a specific product on Amazon and send an email notification if the price drops below a target value.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Sakib-Dalal/Amazon-Price-Tracker.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `main.py` file and update the following variables:

   ```python
   EMAIL = "your-email@gmail.com"
   PASSWORD = "your-app-password"
   PRODUCT_URL = "https://www.amazon.in/gp/product/B0CN1PCYPC/ref=sw_img_1?smid=A11SUS3X5513OU&psc=1"
   TARGET_PRICE = 500.0
   ```

   Replace the values with your Gmail email, [App Password](https://myaccount.google.com/apppasswords), Amazon product URL, and your desired target price.

2. Run the script:

    ```bash
    python main.py
    ```

   The script will check the price every day at 09:00 AM. If the current price is below the target price, it will send an email notification.

## Important Note

- Make sure to enable "Less secure app access" in your Gmail account settings.
- Use an [App Password](https://myaccount.google.com/apppasswords) for secure authentication.
- Please be aware of Amazon's terms of service when scraping data.

Feel free to contribute or customize the code based on your needs. Happy tracking!
