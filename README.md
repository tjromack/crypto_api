# crypto_api
price tracker &amp; alert system with CoinGecko API

Real-time Cryptocurrency Price Tracker and Alert System
This project is designed to periodically fetch and track real-time cryptocurrency prices, market capitalization, and 24-hour price changes. The data is sourced from CoinGecko's API, transformed to a structured format, and then saved to a CSV file for analysis or tracking purposes.

Features
Real-time Data Extraction: Utilizes CoinGecko's API to fetch up-to-date cryptocurrency data.
Data Transformation: Processes raw API data into structured information about cryptocurrency prices, market capitalization, and 24-hour price changes.
Persistent Storage: Stores the structured data in a CSV file, appending new entries at timed intervals.

Python Scripts
alert_system.py: (Placeholder for future features) This module is intended for a system that will notify the user when certain predefined thresholds in cryptocurrency prices are crossed.
api_connector.py: Connects to CoinGecko's API and retrieves raw data for various cryptocurrencies.
data_transformer.py: Processes raw data from the API and structures it into usable formats for further analysis or storage.
data_loader.py: Contains functionality to save transformed data to a CSV file.
loader_sqlite.py: (Placeholder for future features) This module is intended for a system that will allow storage of data into an SQLite database.
main.py: The primary script that orchestrates the extraction, transformation, and loading of cryptocurrency data. It runs in a continuous loop, refreshing data at specified intervals.

How to Run
Ensure you have the required packages installed:
pip install -r requirements.txt

Run the main.py script:
python main.py

The script will run indefinitely, fetching and saving data to the crypto_data.csv file every minute. You can adjust the time interval by changing the sleep duration in main.py.
