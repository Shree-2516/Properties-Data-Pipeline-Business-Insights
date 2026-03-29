import pandas as pd
import os


def clean_data():
    print("🚀 Starting Data Cleaning...")

    # 🔥 Base directory (project root)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    listings_path = os.path.join(BASE_DIR, 'data', 'raw', 'Listings.csv')
    reviews_path = os.path.join(BASE_DIR, 'data', 'raw', 'Reviews.csv')

    # Load data
    listings = pd.read_csv(listings_path, encoding='latin1')
    reviews = pd.read_csv(reviews_path, encoding='latin1')

    # ---------------------------
    # 🔹 Clean listings
    # ---------------------------
    listings = listings.drop_duplicates()

    if 'price' in listings.columns:
        listings['price'] = listings['price'].replace(r'[\$,]', '', regex=True)  # ✅ fixed warning
        listings['price'] = pd.to_numeric(listings['price'], errors='coerce')

    listings.fillna({
        'price': 0,
        'name': 'Unknown'
    }, inplace=True)

    listings.columns = listings.columns.str.strip().str.lower().str.replace(' ', '_')

    # ---------------------------
    # 🔹 Clean reviews
    # ---------------------------
    reviews = reviews.drop_duplicates()

    if 'date' in reviews.columns:
        reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')

    reviews.columns = reviews.columns.str.strip().str.lower().str.replace(' ', '_')

    # ---------------------------
    # 🔹 Save
    # ---------------------------
    output_path = os.path.join(BASE_DIR, 'data', 'processed')
    os.makedirs(output_path, exist_ok=True)

    listings.to_csv(os.path.join(output_path, 'clean_listings.csv'), index=False)
    reviews.to_csv(os.path.join(output_path, 'clean_reviews.csv'), index=False)

    print("✅ Data Cleaning Completed Successfully!")


if __name__ == "__main__":
    clean_data()