DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS listings;

CREATE TABLE listings (
    id BIGINT PRIMARY KEY,
    name TEXT,
    price FLOAT,
    neighbourhood TEXT,
    host_id BIGINT,
    price_per_person FLOAT,
    host_performance_score FLOAT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    listing_id BIGINT,
    comments TEXT,
    review_sentiment TEXT,
    review_date DATE
);