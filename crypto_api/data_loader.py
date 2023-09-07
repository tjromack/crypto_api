import csv
import os

def save_to_csv(data, filename="crypto_data.csv"):
    # Check if the file already exists
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file doesn't exist, write headers
        if not file_exists:
            writer.writerow([
                "Timestamp",
                "bitcoin_Price", "ethereum_Price", "binancecoin_Price", 
                "cardano_Price", "ripple_Price",
                "bitcoin_Market_Cap", "ethereum_Market_Cap", 
                "binancecoin_Market_Cap", "cardano_Market_Cap", 
                "ripple_Market_Cap",
                "bitcoin_24h_Change", "ethereum_24h_Change",
                "binancecoin_24h_Change", "cardano_24h_Change",
                "ripple_24h_Change"
            ])
        
        writer.writerow(data)
