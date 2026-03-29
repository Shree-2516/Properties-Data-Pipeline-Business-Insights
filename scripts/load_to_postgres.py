import pandas as pd
import os
from db_connection import get_engine


def load_data():
    print("🚀 Starting Data Load to PostgreSQL...")

    # 🔥 Base path (works from anywhere)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    listings_path = os.path.join(BASE_DIR, 'data', 'processed', 'clean_listings.csv')
    reviews_path = os.path.join(BASE_DIR, 'data', 'processed', 'clean_reviews.csv')

    # ---------------------------
    # 🔹 Load CSV (optimized)
    # ---------------------------
    print("📂 Reading CSV files...")
    listings = pd.read_csv(listings_path, low_memory=False)
    reviews = pd.read_csv(reviews_path, low_memory=False)

    print(f"Listings rows: {len(listings)}")
    print(f"Reviews rows: {len(reviews)}")

    # ---------------------------
    # 🔹 Get DB engine
    # ---------------------------
    engine = get_engine()

    # ---------------------------
    # 🔹 Load into PostgreSQL (FAST 🚀)
    # ---------------------------
    print("📤 Loading listings table...")
    listings.to_sql(
        'listings',
        engine,
        if_exists='replace',
        index=False,
        chunksize=5000,     # 🔥 faster
        method='multi'      # 🔥 much faster insert
    )

    print("📤 Loading reviews table...")
    reviews.to_sql(
        'reviews',
        engine,
        if_exists='replace',
        index=False,
        chunksize=5000,
        method='multi'
    )

    print("✅ Data Loaded to PostgreSQL Successfully!")


if __name__ == "__main__":
    load_data()