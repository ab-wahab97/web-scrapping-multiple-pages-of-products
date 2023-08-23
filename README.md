# web-scrapping-multiple-pages-of-products
webscrapping multiple pages of product with beautiful soup and request library and then creating a csv file
# Laptop Price Scraper

This Python script scrapes laptop prices and availability from [czone.com.pk](https://www.czone.com.pk/) and saves the data in a CSV file. It uses the requests library to fetch web pages, BeautifulSoup for parsing, and pandas for data manipulation.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Required Python libraries (requests, BeautifulSoup, pandas) installed. You can install them using pip:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/laptop-price-scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd laptop-price-scraper
    ```

3. Run the script:

    ```bash
    python laptop_price_scraper.py
    ```

The script will scrape laptop prices and save the data in a file named `LaptopPrices.csv`.

## Usage

You can modify the script to scrape data from different websites by changing the `url` variable. Additionally, you can customize the data extraction and storage methods as needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request. 

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.


