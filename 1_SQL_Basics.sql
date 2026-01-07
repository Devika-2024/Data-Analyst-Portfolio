--PROJECT : Subscription Data Analysis
--Goal    : Extract high-value 'Pro' tier users from the database

--1. Selecting all columns for orders that were returned and cost more than $100
SELECT *
FROM Sales 
WHERE Status = 'Returned' AND Price > $100;

--2. Calculating Total Revenue grouped by Subscription Tier
SELECT Tier, SUM(monthly_price) as Total_Revenue
FROM subscriptions
GROUP BY Tier;

--3. Counting items sold per store location
SELECT store_location, COUNT(product_id) as total_items_sold
From Sales
GROUP BY store_location;
