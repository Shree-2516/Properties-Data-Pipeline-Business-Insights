import pandas as pd
import os


def feature_engineering():
    print("🚀 Starting Feature Engineering...")

    # 🔥 Base path (fix path issue permanently)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    listings_path = os.path.join(BASE_DIR, 'data', 'processed', 'clean_listings.csv')
    reviews_path = os.path.join(BASE_DIR, 'data', 'processed', 'clean_reviews.csv')

    # Load data
    listings = pd.read_csv(listings_path)
    reviews = pd.read_csv(reviews_path)

    # ---------------------------
    # 🔹 Feature 1: Price per person
    # ---------------------------
    if 'price' in listings.columns and 'accommodates' in listings.columns:
        listings['accommodates'] = listings['accommodates'].replace(0, 1)  # avoid divide by zero
        listings['price_per_person'] = listings['price'] / listings['accommodates']

    # ---------------------------
    # 🔹 Feature 2: Host performance score
    # ---------------------------
    if 'review_scores_rating' in listings.columns:
        listings['host_performance_score'] = listings['review_scores_rating'] / 20

    # ---------------------------
    # 🔹 Feature 3: Review count per listing (BEST replacement 🔥)
    # ---------------------------
    review_counts = reviews.groupby('listing_id').size().reset_index(name='review_count')

    listings = listings.merge(review_counts, on='listing_id', how='left')
    listings['review_count'] = listings['review_count'].fillna(0)

    # ---------------------------
    # 🔹 Save updated data
    # ---------------------------
    listings.to_csv(listings_path, index=False)
    reviews.to_csv(reviews_path, index=False)

    print("✅ Feature Engineering Completed Successfully!")


if __name__ == "__main__":
    feature_engineering()
    