# Amazon Price Tracker

## Introduction

Amazon Price Tracker is a Python script that helps you monitor the price of a specific product on Amazon and sends you an email notification if the price drops below your specified target.

## Prerequisites

Before using the Amazon Price Tracker, make sure you have the following:

- Python installed on your machine
- Necessary Python packages installed (you can install them using `pip install -r requirements.txt`)
- An Amazon product URL that you want to track
- An email address to receive notifications
- An app password for the email account used in the script

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Sakib-Dalal/Amazon-Price-Tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Amazon-Price-Tracker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Open `main.py` in a text editor and update the following variables:

    - `EMAIL`: Your email address
    - `PASSWORD`: Your app password for the email account
    - `PRODUCT_URL`: The URL of the Amazon product you want to track
    - `TARGET_PRICE`: Your desired target price for the product

## Usage

Run the script using the following command:

```bash
python main.py
```

The script will check the price of the specified product on Amazon every day at 09:00 AM. If the current price is below your target price, you will receive an email notification with a link to the product.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request on the [GitHub repository](https://github.com/Sakib-Dalal/Amazon-Price-Tracker).

## Disclaimer

This script is provided as-is and may require adjustments based on changes to the Amazon website structure. Use it responsibly and at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
