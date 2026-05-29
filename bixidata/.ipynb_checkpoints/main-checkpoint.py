import pandas as pd
from datetime import datetime
import googlemaps
from dotenv import load_dotenv 
import os

load_dotenv()

GOOGLEMAPS_API_KEY = os.getenv("GOOGLEMAPS_API_KEY")

BIXI_CSV_PATH = "./DonneesOuvertes2025_010203040506070809101112.csv"


gm = googlemaps.Client(key=GOOGLEMAPS_API_KEY)




def main():
    print("Hello from bixidata!")
    df = pd.read_csv(CSV_PATH, header=0)
#     print(df)
#
#
# if __name__ == "__main__":
#     main()
