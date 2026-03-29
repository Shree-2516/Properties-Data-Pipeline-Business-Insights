-- View listings table
SELECT * FROM listings LIMIT 10;

-- View reviews table
SELECT * FROM reviews LIMIT 10;


-- PRICING ANALYSIS

-- Average price of listings
SELECT AVG(price) AS avg_price FROM listings;

-- Top 10 most expensive listings
SELECT name, price
FROM listings
ORDER BY price DESC
LIMIT 10;

-- Cheapest listings
SELECT name, price
FROM listings
ORDER BY price ASC
LIMIT 10;

-- Average price by location
SELECT neighbourhood, AVG(price) AS avg_price
FROM listings
GROUP BY neighbourhood
ORDER BY avg_price DESC;

-- Price distribution by room type
SELECT room_type, AVG(price) AS avg_price
FROM listings
GROUP BY room_type;


-- CUSTOMER SATISFACTION

-- Average rating overall
SELECT AVG(review_scores_rating) AS avg_rating FROM listings;

-- Top rated listings
SELECT name, review_scores_rating
FROM listings
ORDER BY review_scores_rating DESC
LIMIT 10;

-- Listings with low ratings
SELECT name, review_scores_rating
FROM listings
WHERE review_scores_rating < 50;


-- PERFORMANCE ANALYSIS

-- Listings with highest host performance score
SELECT name, host_performance_score
FROM listings
ORDER BY host_performance_score DESC
LIMIT 10;

-- Listings with most reviews
SELECT listing_id, COUNT(*) AS total_reviews
FROM reviews
GROUP BY listing_id
ORDER BY total_reviews DESC
LIMIT 10;

-- Average reviews per listing
SELECT AVG(review_count)
FROM (
    SELECT listing_id, COUNT(*) AS review_count
    FROM reviews
    GROUP BY listing_id
) sub;




-- LOCATION INSIGHTS

-- Locations with most listings
SELECT neighbourhood, COUNT(*) AS total_listings
FROM listings
GROUP BY neighbourhood
ORDER BY total_listings DESC;

-- Locations with highest average rating
SELECT neighbourhood, AVG(review_scores_rating) AS avg_rating
FROM listings
GROUP BY neighbourhood
ORDER BY avg_rating DESC;

-- Locations with highest revenue potential
SELECT neighbourhood, SUM(price) AS total_revenue
FROM listings
GROUP BY neighbourhood
ORDER BY total_revenue DESC;


-- ADVANCED BUSINESS QUESTIONS

-- Price vs rating relationship
SELECT price, review_scores_rating
FROM listings;

-- High price but low rating listings
SELECT name, price, review_scores_rating
FROM listings
WHERE price > 200 AND review_scores_rating < 60;

-- Best value listings (high rating, low price)
SELECT name, price, review_scores_rating
FROM listings
ORDER BY review_scores_rating DESC, price ASC
LIMIT 10;


-- Top performing listings (combined score)
SELECT name,
(price * host_performance_score) AS performance_score
FROM listings
ORDER BY performance_score DESC
LIMIT 10;