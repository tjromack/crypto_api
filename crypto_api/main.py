import time
from api_connector import get_crypto_data
from data_transformer import transform_data
from data_loader import save_to_csv

def main():
    raw_data = get_crypto_data()
    
    # Transform data to structured format
    prices, market_caps, changes = transform_data(raw_data)
    
    # Get the current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Prepare data for CSV
    data_to_write = [
        timestamp, 
        prices['bitcoin'], prices['ethereum'], prices['binancecoin'], 
        prices['cardano'], prices['ripple'], 
        market_caps['bitcoin'], market_caps['ethereum'], market_caps['binancecoin'], 
        market_caps['cardano'], market_caps['ripple'],
        changes['bitcoin'], changes['ethereum'], changes['binancecoin'],
        changes['cardano'], changes['ripple']
    ]
    
    # Save data to CSV
    save_to_csv(data_to_write)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)  # Sleep for 1 minute(s) (adjust time accordingly to your desired intervals)


